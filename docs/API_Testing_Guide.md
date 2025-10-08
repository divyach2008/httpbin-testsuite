# API Testing Guide for HTTPBin

This guide explains how to test the HTTPBin API endpoints.

## Endpoints

### GET /ip
Returns the origin IP address.

### GET /user-agent
Returns the user agent string.

### POST /post
Returns the posted data.

### GET /headers
Returns request headers.

### GET /status/{code}
Returns the specified HTTP status code.

### GET /delay/{seconds}
Delays the response by the specified number of seconds.

## Testing Strategy

- Validate response codes
- Check expected fields
- Simulate edge cases (e.g., status 418, delay)
