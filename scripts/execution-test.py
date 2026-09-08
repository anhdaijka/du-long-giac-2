#!/usr/bin/env python3
"""Regression tests for execution-guard.py."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUARD = ROOT / "scripts" / "execution-guard.py"


def run(root: Path, manifest: Path, *, require_complete: bool = False) -> subprocess.CompletedProcess[str]:
    args = [sys.executable, str(GUARD), "--manifest", str(manifest)]
    if require_complete:
        args.append("--require-complete")
    return subprocess.run(args, cwd=root, text=True, capture_output=True, check=False)


def assert_code(label: str, result: subprocess.CompletedProcess[str], expected: int) -> None:
    if result.returncode != expected:
        print(f"[FAIL] {label}: expected exit {expected}, got {result.returncode}")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)
    print(f"[PASS] {label}")


def write_manifest(root: Path, data: dict) -> Path:
    path = root / "execution.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def base_manifest() -> dict:
    return {
        "manifest_id": "test_execution",
        "scope": "fixture",
        "deliverables": [
            {
                "id": "D01",
                "description": "Create first artifact",
                "requires": [],
                "checks": [{"type": "file_nonempty", "path": "out/first.txt"}],
            },
            {
                "id": "D02",
                "description": "Create dependent artifact",
                "requires": ["D01"],
                "checks": [{"type": "file_nonempty", "path": "out/second.txt"}],
            },
        ],
    }


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="novel-os-execution-") as temp:
        root = Path(temp)
        (root / "out").mkdir()

        manifest = base_manifest()
        path = write_manifest(root, manifest)
        result = run(root, path)
        assert_code("tracking mode reports incomplete work without schema failure", result, 0)
        if "[INCOMPLETE] D01" not in result.stdout or "[BLOCKED] D02" not in result.stdout:
            print("[FAIL] computed statuses did not expose incomplete/blocking state")
            print(result.stdout)
            return 1
        print("[PASS] dependency blocking is verifier-computed")

        result = run(root, path, require_complete=True)
        assert_code("require-complete rejects missing deliverables", result, 1)

        (root / "out" / "first.txt").write_text("first\n", encoding="utf-8")
        result = run(root, path, require_complete=True)
        assert_code("downstream missing artifact keeps plan incomplete", result, 1)
        if "[COMPLETE] D01" not in result.stdout or "[INCOMPLETE] D02" not in result.stdout:
            print("[FAIL] expected D01 complete and D02 incomplete")
            print(result.stdout)
            return 1
        print("[PASS] partial execution cannot masquerade as full completion")

        (root / "out" / "second.txt").write_text("second\n", encoding="utf-8")
        result = run(root, path, require_complete=True)
        assert_code("all verified deliverables complete the plan", result, 0)

        manifest = base_manifest()
        manifest["deliverables"][0]["status"] = "done"
        path = write_manifest(root, manifest)
        result = run(root, path)
        assert_code("self-certified deliverable status is rejected", result, 1)

        manifest = base_manifest()
        manifest["status"] = "complete"
        path = write_manifest(root, manifest)
        result = run(root, path)
        assert_code("self-certified manifest status is rejected", result, 1)

        manifest = base_manifest()
        manifest["deliverables"][0]["checks"] = [
            {"type": "command", "command": "echo trust-me"}
        ]
        path = write_manifest(root, manifest)
        result = run(root, path)
        assert_code("arbitrary command checks are rejected", result, 1)

        manifest = base_manifest()
        manifest["deliverables"][0]["requires"] = ["D02"]
        path = write_manifest(root, manifest)
        result = run(root, path)
        assert_code("dependency cycles are rejected", result, 1)

    print("\n[EXECUTION TEST PASS] Completion is verifier-owned and partial plans cannot self-certify.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
