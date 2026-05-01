import pytest
from dt_ai.ai import parse_ai_response

def test_aesthetic_prompt_mentorship():
    from dt_ai.ai import AESTHETIC_PROMPT
    assert "mentor" in AESTHETIC_PROMPT.lower()
    assert "educational" in AESTHETIC_PROMPT.lower()
    assert "exposure" in AESTHETIC_PROMPT.lower()

def test_parse_ai_response_valid():
    text = "```json\n{\"test\": 1}\n```"
    result = parse_ai_response(text)
    assert result["test"] == 1

def test_parse_ai_response_with_text():
    text = "Here is some text. ```json\n{\"foo\": \"bar\"}\n``` And more text."
    result = parse_ai_response(text)
    assert result["foo"] == "bar"
