import requests

BASE_URL = "http://localhost"

def test_status_418():
    response = requests.get(f"{BASE_URL}/status/418")
    assert response.status_code == 418
    assert "I'm a teapot" in response.text
