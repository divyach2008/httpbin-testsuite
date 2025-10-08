import requests

BASE_URL = "http://localhost"

def test_delay_response():
    response = requests.get(f"{BASE_URL}/delay/2", timeout=5)
    assert response.status_code == 200
    assert "delay" in response.url
