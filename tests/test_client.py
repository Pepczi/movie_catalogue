from main import app
from unittest.mock import Mock
import pytest

@pytest.mark.parametrize("list_type, result", [ ("/?list_type=popular", "movie/popular"),
                                                ("/?list_type=upcoming", "movie/upcoming"),
                                                ("/?list_type=top_rated", "movie/top_rated"),
                                                ("/?list_type=now_playing", "movie/now_playing")])

def test_hompepage(monkeypatch, list_type, result):
    api_mock = Mock(return_value={"results": ["550", "124905", "475557"]})
    monkeypatch.setattr("tmdb_client.call_tmdb", api_mock)

    with app.test_client() as client:
        response = client.get(list_type)
        assert response.status_code == 200
        api_mock.assert_called_once_with(result)