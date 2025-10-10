#  HTTPBin API Test Suite

This repository contains automated tests for the [HTTPBin API](https://github.com/postmanlabs/httpbin), designed to run locally using Docker and Python.

## Getting Started

### Prerequisites

- Docker
- Python 3.8+
- pip

### Setup

1. Clone this repository:
   
   clone the above mentioned repository
   
2.	Start the HTTPBin API using Docker:

docker-compose up -d

3.	Install dependencies:

pip install -r requirements.txt

4.	Run tests:

pytest tests/
