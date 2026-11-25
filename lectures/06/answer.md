# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：
- STEP 2 の [tool call]：
- STEP 3 の [tool call]：
- STEP 4 の [tool call]：
- 気づき・疑問：

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

-- 取り組んだレベル：基礎
- やったこと：app/mcp_server.py に server.tool()(tools.get_lecture_summary) の1行を足し、get_lecture_summary を MCP のツールとして公開した。エージェント側（app/mcp_agent.py と app/mcp_servers.json）は変えていない。
- 結果：
  - --list-tools：モデルに見えているツールが 1 個 → 2 個になり、glossary_get_lecture_summary が増えた
  - --trace「第2回では何を学びますか？」：[tool call] glossary_get_lecture_summary({'lecture': 2})（モデル応答 2 回、入力 1,274 / 出力 230 tokens）
  - uv run pytest -q：21 passed
- 気づき・疑問：エージェント側を1文字も変えていないのに、なぜツールが増えたのか
