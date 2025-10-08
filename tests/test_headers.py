import requests

BASE_URL = "http://localhost"

def test_custom_headers():
    headers = {"X-Test-Header": "TestValue"}
    response = requests.get(f"{BASE_URL}/headers", headers=headers)
    assert response.status_code == 200
    assert response.json()["headers"]["X-Test-Header"] == "TestValue"
