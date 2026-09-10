# Đề xuất chapter architecture Quyển II — áp lực của lời đồn

Trạng thái: `AUTHOR-DEFAULTED PLANNING / D52-R78 / NOT A CHAPTER PLAN / NOT A SCENE PLAN / NOT PROSE / NOT CANON`.

## Mục tiêu và trần thẩm quyền

Quyển II đưa pressure quanh Du Long từ lời báo/bang phái thành một lần hợp tác vật lý hữu hạn đầu tiên của trio, rồi bàn giao sang Phục Ngưu. Architecture này chỉ phân bố **chức năng kể chuyện có provenance**; không nhận rằng source đã cho trio tham gia mọi task, không linearize game, và không làm đầy custody Du Long, Huyền Nguyệt, chronology, venue hay outcome.

Đầu vào bắt buộc: [functional architecture đã duyệt](chapter-architecture-phase-spec-volume-ii.md), [source-window map](writer-preflight-volume-ii/volume-ii-source-window-map.md), [coverage ledger](writer-preflight-volume-ii/volume-ii-source-window-coverage-ledger.md), [deep survey Hạ/density](writer-preflight-volume-ii/volume-ii-ha-density-deep-survey.md), và macro authority R-66–R-70. SQLite packet/query-result là authority; phân phối POV là adaptation planning, không là game fact.

## Kết luận density

Architecture đề xuất **7 candidate-function**, trong đó hai hàng chỉ là context/transition. Đây là dải chức năng 5–7, **không phải seven-chapter plan**, không quota POV, không chronology, và không yêu cầu tất cả xuất hiện như một chương độc lập. Một row chỉ tách khi có hai causal turn độc lập hoặc dự kiến vượt 5.500 từ; chỉ gộp khi knowledge boundary, NPC agency và hard stop còn nguyên.

| Dải | Suy ra được | Không suy ra được |
| --- | --- | --- |
| Minimum viable | 5 containers: pursuit pressure, social cost, Hạ context, limited convergence, Phục Ngưu handoff. | Không có “5 chương chuẩn”. |
| Candidate band | 5–7 containers khi hai report và/hoặc living-lore có causal return riêng. | Không có baseline, title hay chapter number. |
| Overflow | Trên 7 chỉ khi source window mới đã deep-read chứng minh causal need. | Không đào source để đủ count. |

## Candidate-function matrix

`primary aperture` là **proposed novelization allocation**, không phải source attribution và chưa được writer dùng. Mỗi source claim vẫn bị giới hạn bởi receipt đúng window.

| Candidate | Function / kênh | Primary aperture đề xuất | Evidence envelope | Entry → exit được phép | Hard stop |
| --- | --- | --- | --- | --- | --- |
| `V2-ARCH-CAND-01` | Đưa lời Bạch Thu Lâm về Diêm Bang/Từ Bân Kiếm và pressure Du Long vào không gian công cộng qua relay/aftermath, không diễn avatar objective. | Tiêu Phùng **proposed**, hoặc `DOCUMENT/ORGANIZATION` nếu không có POV-safe relay. | `V2-SW-04`: `SOURCE REPORT + GAME EVENT`. | Tin/báo cáo scoped tồn tại → Tiêu hiểu tên mình/bảo vật đang bị người khác dùng làm pressure, không biết motive hay custody. | Không gán avatar action cho Tiêu; không định danh network Diêm Bang, venue, combat, victory hay objective truth của lời báo. |
| `V2-ARCH-CAND-02` | Đặt report Bang Nguyên như pressure song song cần kiểm an ninh, không gộp với Diêm Bang thành cùng plot. | Tĩnh Xuyên **proposed**, hoặc `DOCUMENT/AFTERMATH`. | `V2-SW-05`: `SOURCE REPORT + GAME EVENT`. | Một report/scouting scope riêng → Tĩnh chỉ có thể chọn mức đề phòng/hộ tống trong phạm vi chức trách được author approve. | Không xác nhận Lôi Lão Cửu report là đúng, biến đám người thành phe thống nhất, hay gán event/chiến quả cho Tĩnh. |
| `V2-ARCH-CAND-03` | Cho thấy giá cộng đồng của thông tin/quyền lực bằng một return đúng scope, để Hạ có áp lực chăm sóc mà không thành “ca bệnh Hạ giải quyết”. | Hạ Nương **approved narrow Bridge ceiling**. | `V2-HS-01`; optional `V2-SW-02/03` chỉ khi chọn receipt riêng. | Hạ quan sát/đối chiếu/chăm sóc giới hạn → hiểu giới hạn chứng cứ và cá nhân, không cure/result. | Không chẩn đoán khách quan, nêu cơ chế Hàn Diêm, kết thúc bệnh, nhận credit avatar, hoặc gom report cùng nơi/cùng lúc. |
| `V2-ARCH-CAND-04` | Để giang hồ có chiều sâu qua mẩu ký ức/tư liệu Tàng Kiếm–Độc Cô Kiếm, chỉ khi đổi cách hiểu tin đồn hiện tại. | `LIVING-LORE / WITNESS`; không mặc định POV trio. | `V2-SW-06`: `SOURCE REPORT / LEGENDARY LORE`. | Người kể/tư liệu có scope → reader nhận layer bất định, không handoff toàn tri cho trio. | Không xác nhận historical fact, cái chết/trận Thái Thạch, di vật, võ công, genealogy hay tạo cao thủ mới. Bỏ nếu không causal return. |
| `V2-ARCH-CAND-05` | **Limited physical convergence**: ba người cùng đáp một pressure tối thiểu, trao đổi đúng knowledge ceiling, rồi tách ra không thành party. | Trio, nhưng chỉ `FUNCTIONAL BRIDGE`. | R-67/CMQ-01 + V2CAQ-03; không direct game row cho scene. | Knowledge riêng → hợp tác hữu hạn → exit non-party, không shared custody/truth. | Không chọn sender, venue, duration, dialogue, combat, custody reveal, outcome, quan hệ bền vững hay chronology. Detail chờ scene-plan gate. |
| `V2-ARCH-CAND-06` | Đặt y/giang hồ ở ngưỡng Phục Ngưu để Hạ thấy tri thức và người chữa trị cũng bị đường đi/quyền lực chi phối, không thành người thừa kế vật phẩm. | Hạ Nương **approved narrow Bridge ceiling**, hoặc `REPORT/DOCUMENT`. | `V2-HS-02`: `DIRECT SOURCE CONTEXT`. | Report/context Lão Mặc Nhĩ, đồ phổ, kim châm → Hạ chỉ đối chiếu evidence/chăm sóc hiện hữu. | Không để Hạ gặp/cứu/nhận đồ, đọc/thi triển vật phẩm; không hiệu lực y thuật, liên minh, rescue outcome hay timeline. Bỏ nếu exit đạt mà không cần. |
| `V2-ARCH-CAND-07` | Bàn giao hậu Thái Tổ Bảo Khố sang dựng Phục Ngưu bằng organization action/document/aftermath, giữ agency Bạch Thu Lâm và thế giới ngoài trio. | `ORGANIZATION / DOCUMENT / AFTERMATH`; không mặc định POV. | `V2-SW-09`: `DIRECT GAME EVENT + SOURCE REPORT + GAMEPLAY TRANSLATION`. | Source transition report → thế giới/tổ chức đổi từ tranh bảo sang preparation pressure. | Không gọi lời Bạch Thu Lâm là historical/objective fact; không command/authority, secrecy, travel, teleport, dungeon, resource count, combat hay trio participation. |

## Causal braid — partial order, không chronology

```text
V2-ARCH-CAND-01 ─┐
                  ├─> V2-ARCH-CAND-05 ─> V2-ARCH-CAND-07
V2-ARCH-CAND-02 ─┘

V2-ARCH-CAND-03 ───> social-cost / evidence ceiling; đứng trước hoặc sau 01/02
V2-ARCH-CAND-04 ───> optional living-lore return; không prerequisite
V2-ARCH-CAND-06 ───> optional Phục Ngưu context; không prerequisite
```

Chỉ khóa dependency chức năng: convergence không xảy ra trước khi hai pressure độc lập tồn tại trong architecture; handoff Phục Ngưu không cần “thắng lợi” của trio. Không suy ra ngày, đường đi, nơi chốn, thứ tự report, hoặc rằng Hạ/Tĩnh/Tiêu biết cùng một điều.

## Knowledge và fact-safety boundary

1. `GAME FACT` chỉ từ SQLite receipt đúng window, giữ speaker/task scope.
2. `HISTORICAL FACT` không được suy từ NPC report, legendary lore hay game alt-history.
3. `NOVELIZATION BRIDGE`: CAND-03/06 chỉ có trần R-76; CAND-05 chỉ functional bridge R-74. Mọi implementation khác cần decision mới.
4. `READER_KNOWLEDGE != CHARACTER_KNOWLEDGE`; document/witness cần sender, recipient, scope.
5. `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED`; `HUYEN_NGUYET_MECHANISM = DEFERRED`; canon Tĩnh Xuyên/Mộc Nhất Lâu–Ân Đồng ngoài scope.
6. Không dùng `V2-SW-01`, `07`, `08`, phần chưa đọc của `10/11`, hay T118/S267 để lấp density.

## Resolution mặc định của V2CABQ-01–06

| ID | Resolution planning được áp dụng | Lưu ý writer sau này |
| --- | --- | --- |
| `V2CABQ-01` | Giữ 7 candidate-function như architecture band; `COUNT = UNRESOLVED`. | Không biến thành seven-chapter count. |
| `V2CABQ-02` | CAND-01/02 dùng proposed Tiêu/Tĩnh relay/aftermath allocation; không avatar mapping/game fact. | Writer hỏi khi cần sender/recipient/venue hay outcome cụ thể. |
| `V2CABQ-03` | CAND-03/06 chỉ theo ceiling Hạ R-76; CAND-06 optional. | Writer hỏi khi cần medical fact, direct encounter, possession/use hoặc case closure. |
| `V2CABQ-04` | CAND-04 là optional reservoir, chỉ vào khi causal return được brief chứng minh. | Writer không tự gọi legendary report là history. |
| `V2CABQ-05` | CAND-05 chỉ functional convergence. | Writer hỏi khi cần scene/venue/dialogue/combat/outcome. |
| `V2CABQ-06` | CAND-07 là organization/document/aftermath handoff. | Writer hỏi khi cần trio participation, authority hay historical closure. |

## Bước kế tiếp tự động

Dựng `chapter-architecture-volume-ii/` projection và coverage ledger `V2-CH-*` ngay theo các resolution trên. Việc đó vẫn không tạo chapter number/title/brief, scene plan, prose, canon hay exact chronology. Gemini chỉ dùng ledger sau receipt theo candidate và phải escalate mọi proposition vượt hard stop.
