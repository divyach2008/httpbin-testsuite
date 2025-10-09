import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "http://localhost"
NUM_REQUESTS = 100  # Total number of requests to simulate
CONCURRENCY = 20    # Number of concurrent threads

def make_request(session, url):
    start = time.time()
    try:
        response = session.get(url)
        latency = time.time() - start
        return {
            "status": response.status_code,
            "latency": latency
        }
    except Exception as e:
        return {
            "status": "error",
            "latency": None,
            "error": str(e)
        }

def test_stress_get_ip():
    url = f"{BASE_URL}/ip"
    results = []
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        with requests.Session() as session:
            futures = [executor.submit(make_request, session, url) for _ in range(NUM_REQUESTS)]
            for future in as_completed(futures):
                result = future.result()
                results.append(result)

    success_count = sum(1 for r in results if r["status"] == 200)
    error_count = sum(1 for r in results if r["status"] != 200)
    avg_latency = sum(r["latency"] for r in results if r["latency"]) / success_count

    print(f"\nStress Test Results for GET /ip")
    print(f"Total Requests: {NUM_REQUESTS}")
    print(f"Successful: {success_count}")
    print(f"Failed: {error_count}")
    print(f"Average Latency: {avg_latency:.3f} seconds")

    assert success_count > 0
