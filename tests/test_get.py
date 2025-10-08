import requests

BASE_URL = "http://localhost"

def test_get_ip():
    response = requests.get(f"{BASE_URL}/ip")
    assert response.status_code == 200
    assert "origin" in response.json()

def test_get_user_agent():
    response = requests.get(f"{BASE_URL}/user-agent")
    assert response.status_code == 200
    assert "user-agent" in response.json()
