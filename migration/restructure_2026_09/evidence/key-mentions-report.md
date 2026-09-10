# Key source mentions — generated evidence

Status: non-canonical locator evidence. A hit preserves where text occurs; it does not make a speaker claim objectively true.

- SQLite: `story_database.sqlite3` (b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0)
- Result rows: `key-mentions.tsv`
- Query parameter for each run: `%<term>%`

## Query

```sql
WITH narrative_fields AS (
    SELECT task_id, NULL AS sub_id, 'tasks' AS source_table,
           task_id AS row_id, 'name' AS source_field, name AS source_text
      FROM tasks
    UNION ALL
    SELECT task_id, NULL, 'tasks', task_id, 'describe_cleaned', describe_cleaned
      FROM tasks
    UNION ALL
    SELECT task_id, sub_id, 'subtasks', sub_id, 'name', name
      FROM subtasks
    UNION ALL
    SELECT task_id, sub_id, 'subtasks', sub_id, 'describe_cleaned', describe_cleaned
      FROM subtasks
    UNION ALL
    SELECT s.task_id, st.sub_id, 'steps', st.id, 'instruction', st.instruction
      FROM steps AS st JOIN subtasks AS s ON s.sub_id = st.sub_id
    UNION ALL
    SELECT s.task_id, st.sub_id, 'steps', st.id, 'target_params', st.target_params
      FROM steps AS st JOIN subtasks AS s ON s.sub_id = st.sub_id
    UNION ALL
    SELECT s.task_id, d.sub_id, 'dialogues', d.id, 'cleaned_text', d.cleaned_text
      FROM dialogues AS d JOIN subtasks AS s ON s.sub_id = d.sub_id
)
SELECT task_id, sub_id, source_table, row_id, source_field, source_text
  FROM narrative_fields
 WHERE COALESCE(source_text, '') LIKE ?
 ORDER BY task_id, sub_id, source_table, row_id, source_field
```

## Results

| Term | Matching rows | Distinct tasks |
| --- | ---: | ---: |
| Du Long Giác | 160 | 26 |
| Thái Tổ Bảo Khố | 11 | 2 |
| Hán Thủy | 23 | 8 |
| Tiêu Lăng Phong | 0 | 0 |
| Lệ Thu Thủy | 23 | 3 |
| Lịch Thu Thủy | 2 | 2 |

Every result row records task/subtask, source table, source row ID, field and bounded context. Read the complete source row from SQLite or its Arc packet before interpreting the claim.
