// Kiếm Thế 2 - Web Reader App Logic
let currentFontSize = 14;
let activeItemKey = 'arc_00';

document.addEventListener('DOMContentLoaded', () => {
  initNav();
  renderCurrentView();
  bindEvents();
});

function initNav() {
  const navTree = document.getElementById('navTree');
  if (!window.STORY_DATA) return;
  
  let html = '';
  
  // 1. Chính tuyến
  html += '<div class="nav-group-title">📜 13 Hồi Chính Tuyến</div>';
  window.STORY_DATA.arcs.forEach(arc => {
    html += `<div class="nav-item ${arc.key === activeItemKey ? 'active' : ''}" data-type="arc" data-key="${arc.key}">${arc.title}</div>`;
  });

  // 2. Quân Doanh
  html += '<div class="nav-group-title">⚔️ 4 Đại Quân Doanh</div>';
  window.STORY_DATA.armycamps.forEach(camp => {
    html += `<div class="nav-item" data-type="camp" data-key="${camp.key}">${camp.title}</div>`;
  });

  // 3. Phụ Tuyến
  html += '<div class="nav-group-title">🍃 Phụ Tuyến & Giang Hồ</div>';
  html += `<div class="nav-item" data-type="linktask" data-key="linktask">Truyện Ngắn Bao Vạn Đồng</div>`;
  html += `<div class="nav-item" data-type="ambient" data-key="ambient">Phong Thổ 30 Thành Thị (720 NPC)</div>`;

  navTree.innerHTML = html;

  // Click handler
  navTree.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      navTree.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
      item.classList.add('active');
      activeItemKey = item.getAttribute('data-key');
      const itemType = item.getAttribute('data-type');
      renderView(itemType, activeItemKey);
    });
  });
}

function renderCurrentView() {
  renderView('arc', activeItemKey);
}

function renderView(type, key) {
  const container = document.getElementById('contentContainer');
  const titleElem = document.getElementById('currentViewTitle');
  document.getElementById('readingArea').scrollTop = 0;

  if (type === 'arc') {
    const arc = window.STORY_DATA.arcs.find(a => a.key === key);
    if (!arc) return;
    titleElem.textContent = arc.title;
    
    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">${arc.title}</h1>
        <div class="chapter-summary">${arc.summary}</div>
      </div>
    `;

    arc.tasks.forEach(t => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">[Nhiệm Vụ #${String(t.task_id).padStart(4, '0')}] ${t.name}</div>
            <div class="task-badges">
              <span class="badge badge-gold">${t.category}</span>
              <span class="badge">${t.subs.length} phân đoạn</span>
            </div>
          </div>
          <div class="task-body">
            <div class="task-desc">${t.describe_cleaned}</div>
            ${t.subs.map(s => `
              <div class="subtask-box">
                <div class="subtask-title">
                  <span>Phân đoạn #${String(s.sub_id).padStart(4, '0')}: ${s.name}</span>
                  <span class="subtask-giver">Người giao: ${s.dialog_npc_name || 'Hệ thống'}</span>
                </div>
                <div class="subtask-steps">${s.describe_cleaned}</div>
                ${s.dialogues && s.dialogues.length > 0 ? `
                  <div class="dialogue-section">
                    <div class="dialogue-title">Kịch bản lời thoại:</div>
                    ${s.dialogues.map(d => `<div class="dialogue-bubble"><strong>[${d.phase.toUpperCase()}]:</strong><br>${d.text}</div>`).join('')}
                  </div>
                ` : ''}
                <div class="provenance-tag">Nguồn: ${s.file_path}</div>
              </div>
            `).join('')}
            <div class="provenance-tag" style="margin-top:14px;">Task file: ${t.file_path}</div>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } else if (type === 'camp') {
    const camp = window.STORY_DATA.armycamps.find(c => c.key === key);
    if (!camp) return;
    titleElem.textContent = camp.title;

    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">${camp.title}</h1>
        <div class="chapter-summary">${camp.summary}</div>
      </div>
      <h2 style="color:var(--gold-primary); margin: 24px 0 16px;">1. Các Nhiệm Vụ Quân Doanh (XML Tasks)</h2>
    `;
    
    camp.tasks.forEach(t => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">[Nhiệm Vụ #${String(t.task_id).padStart(4, '0')}] ${t.name}</div>
            <span class="badge badge-gold">${t.category}</span>
          </div>
          <div class="task-body">
            <div class="task-desc">${t.describe_cleaned}</div>
            ${t.subs.map(s => `
              <div class="subtask-box">
                <div class="subtask-title">${s.name}</div>
                <div class="subtask-steps">${s.describe_cleaned}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    });

    html += `<h2 style="color:var(--gold-primary); margin: 32px 0 16px;">2. Kịch Bản Lời Thoại Boss & Cạm Bẫy (LUA)</h2>`;
    camp.lores.forEach(l => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">${l.section}</div>
            <span class="badge">${l.type}</span>
          </div>
          <div class="task-body">
            <div class="dialogue-bubble">${l.text}</div>
            <div class="provenance-tag">Nguồn: ${l.file}</div>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } else if (type === 'linktask') {
    titleElem.textContent = 'Truyện Ngắn Nghĩa Quân Bao Vạn Đồng';
    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">Truyện Ngắn Nghĩa Quân Bao Vạn Đồng</h1>
        <div class="chapter-summary">50 mẩu truyện ngắn ghi nhận tình hình chiến sự, nghĩa cử giang hồ và đời sống bá tánh thời Tống - Kim.</div>
      </div>
    `;
    window.STORY_DATA.linktask.forEach(lt => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">Truyện #${lt.index}: ${lt.cat_name}</div>
            <span class="badge badge-gold">Nghĩa Quân</span>
          </div>
          <div class="task-body">
            <div class="dialogue-bubble">${lt.text}</div>
            <div class="provenance-tag">Nguồn: ${lt.file}</div>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } else if (type === 'ambient') {
    titleElem.textContent = 'Phong Thổ Võ Lâm: 720 Đối Thoại Đời Thường Khắp 30 Thành Thị';
    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">Phong Thổ Võ Lâm: 720 Đối Thoại Đời Thường</h1>
        <div class="chapter-summary">Đàm đạo của các chủ quán, thương gia, tiếp dẫn môn phái tại 30 thành thị lớn thời Nam Tống.</div>
      </div>
    `;
    window.STORY_DATA.ambient_maps.forEach(m => {
      html += `
        <h2 style="color:var(--gold-primary); margin: 28px 0 14px;">Bản Đồ: ${m.map_name} (Map ID: ${m.map_id})</h2>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 24px;">
          ${m.dialogues.map(d => `
            <div class="subtask-box">
              <div class="subtask-title">Lớp NPC: ${d.npc_class}</div>
              <div style="font-size:13.5px; color:#e2e8f0; line-height:1.5; margin-bottom:8px;">${d.msg}</div>
              ${d.options ? `<div style="font-size:12px; color:#94a3b8;"><em>Tương tác: ${d.options}</em></div>` : ''}
            </div>
          `).join('')}
        </div>
      `;
    });
    container.innerHTML = html;
  }
}

function bindEvents() {
  document.getElementById('btnZoomIn').addEventListener('click', () => {
    if (currentFontSize < 22) {
      currentFontSize += 1.5;
      document.getElementById('contentContainer').style.fontSize = currentFontSize + 'px';
    }
  });

  document.getElementById('btnZoomOut').addEventListener('click', () => {
    if (currentFontSize > 12) {
      currentFontSize -= 1.5;
      document.getElementById('contentContainer').style.fontSize = currentFontSize + 'px';
    }
  });

  document.getElementById('btnZenMode').addEventListener('click', () => {
    const sidebar = document.getElementById('sidebar');
    const isHidden = sidebar.style.display === 'none';
    sidebar.style.display = isHidden ? 'flex' : 'none';
  });

  // Tìm kiếm tức thì
  const searchInput = document.getElementById('searchInput');
  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.trim().toLowerCase();
    if (!q) {
      renderCurrentView();
      return;
    }

    const container = document.getElementById('contentContainer');
    document.getElementById('currentViewTitle').textContent = `Kết quả tìm kiếm: "${q}"`;

    let hits = [];
    window.STORY_DATA.arcs.forEach(arc => {
      arc.tasks.forEach(t => {
        const matchTitle = t.name.toLowerCase().includes(q);
        const matchDesc = t.describe_cleaned.toLowerCase().includes(q);
        const matchSub = t.subs.some(s => s.name.toLowerCase().includes(q) || s.describe_cleaned.toLowerCase().includes(q) || (s.dialog_npc_name && s.dialog_npc_name.toLowerCase().includes(q)));
        if (matchTitle || matchDesc || matchSub) {
          hits.push({ arcTitle: arc.title, task: t });
        }
      });
    });

    if (hits.length === 0) {
      container.innerHTML = `<div style="padding: 40px; text-align: center; color: #94a3b8;">Không tìm thấy kết quả nào khớp với "${q}".</div>`;
      return;
    }

    let html = `<div style="margin-bottom: 20px; color: var(--gold-primary); font-size: 15px;">Tìm thấy <strong>${hits.length}</strong> nhiệm vụ phù hợp:</div>`;
    hits.forEach(({ arcTitle, task: t }) => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">[Nhiệm Vụ #${String(t.task_id).padStart(4, '0')}] ${t.name}</div>
            <span class="badge badge-gold">${arcTitle}</span>
          </div>
          <div class="task-body">
            <div class="task-desc">${t.describe_cleaned}</div>
            ${t.subs.map(s => `
              <div class="subtask-box">
                <div class="subtask-title">${s.name} (Người giao: ${s.dialog_npc_name || 'Hệ thống'})</div>
                <div class="subtask-steps">${s.describe_cleaned}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  });
}
