from unittest.mock import patch, MagicMock
from app.services import fact_checker


@patch("app.services.fact_checker.requests.get")
def test_fact_checker_returns_summary(mock_get):
    """Test the successful API response."""

    mock_response = MagicMock()
    mock_response.json.return_value = {
        "extract": "Artificial intelligence (AI) is intelligence demonstrated by machines."
    }
    mock_get.return_value = mock_response

    summary = fact_checker.fact_check("Artificial Intelligence")

    assert isinstance(summary, str)
    assert len(summary) > 10
    assert "Artificial intelligence" in summary


@patch("app.services.fact_checker.requests.get")
def test_fact_checker_missing_extract(mock_get):
    """Test when the API response does not contain an extract."""

    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response

    summary = fact_checker.fact_check("Unknown Topic")

    assert summary == "No summary found."


@patch("app.services.fact_checker.requests.get")
def test_fact_checker_handles_request_error(mock_get):
    """Test network or request failures."""

    mock_get.side_effect = Exception("Connection failed")

    summary = fact_checker.fact_check("Artificial Intelligence")

    assert summary == "Fact-checking failed."