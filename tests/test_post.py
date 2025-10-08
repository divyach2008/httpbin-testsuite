import requests

BASE_URL = "http://localhost"

def test_post_json():
    payload = {"name": "test"}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    assert response.status_code == 200
    assert response.json()["json"] == payload
