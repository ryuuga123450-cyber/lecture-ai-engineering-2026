"""素のLLMへの質問処理のテスト（LLMもAPIキーも使わない）。"""

from types import SimpleNamespace
from unittest.mock import Mock

from app import ask as ask_module


def _mock_client(response, monkeypatch):
    models = SimpleNamespace(generate_content=Mock(return_value=response))
    client = SimpleNamespace(models=models)
    monkeypatch.setattr(ask_module.genai, "Client", Mock(return_value=client))
    monkeypatch.setattr(ask_module, "get_api_key", Mock(return_value="test-key"))


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        text="answer",
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=7,
        ),
    )
    _mock_client(response, monkeypatch)

    assert ask_module.ask("question") == "answer"
    assert capsys.readouterr().out == "[トークン数] 入力: 12, 出力: 7\n"


def test_ask_reports_missing_token_usage(monkeypatch, capsys):
    response = SimpleNamespace(text="answer", usage_metadata=None)
    _mock_client(response, monkeypatch)

    assert ask_module.ask("question") == "answer"
    assert capsys.readouterr().out == "[トークン数] 利用量情報を取得できませんでした\n"
