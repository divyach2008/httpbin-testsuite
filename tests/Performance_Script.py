import requests
import time
import csv

BASE_URL = "http://localhost"
REPORT_FILE = "test_report.csv"

# Define your test cases
test_cases = [
    {"name": "GET /ip", "url": f"{BASE_URL}/ip"},
    {"name": "GET /user-agent", "url": f"{BASE_URL}/user-agent"},
    {"name": "GET /headers", "url": f"{BASE_URL}/headers"},
    {"name": "GET /delay/2", "url": f"{BASE_URL}/delay/2"},
    {"name": "GET /redirect/1", "url": f"{BASE_URL}/redirect/1", "allow_redirects": True}
]

# Prepare CSV file
with open(REPORT_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Test Name", "URL", "Status Code", "Success", "Latency (s)", "Error"])

    for test in test_cases:
        start = time.time()
        try:
            response = requests.get(test["url"], allow_redirects=test.get("allow_redirects", False))
            latency = round(time.time() - start, 4)
            success = response.status_code == 200
            writer.writerow([test["name"], test["url"], response.status_code, success, latency, ""])
            print(f"{test['name']} ✅ - {latency}s")
        except Exception as e:
            latency = round(time.time() - start, 4)
            writer.writerow([test["name"], test["url"], "N/A", False, latency, str(e)])
            print(f"{test['name']} ❌ - Error: {e}")
