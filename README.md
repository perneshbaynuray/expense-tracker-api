# Expense Tracker API

A lightweight HTTP REST API service built for tracking expenses for INF 345 Milestone 1.

---

## Description

The **Expense Tracker API** is a simple backend service for managing expenses without external database dependencies.

### Endpoints
- **`GET /`**: Entrypoint returning service status.
- **`GET /healthz`**: Liveness probe returning `200 OK`.
- **`GET /expenses`**: Returns the count of expense items.

---

## Code Breakdown & Line-by-Line Explanations

### 1. `src/server.py` — Application Server

```python
import os  # Access environment variables (e.g., $PORT)
from http.server import BaseHTTPRequestHandler, HTTPServer  # Built-in HTTP server modules

EXPENSES = ["groceries", "transport", "utilities"]  # In-memory mock data array


class Handler(BaseHTTPRequestHandler):  # Custom request handler class
    def do_GET(self):  # Handles incoming HTTP GET requests
        if self.path == "/healthz":  # Health check endpoint
            self._send(200, b"ok")  # Returns 200 OK
        elif self.path == "/":  # Root endpoint
            self._send(200, b"expense tracker api")  # Returns service welcome message
        elif self.path == "/expenses":  # Expenses endpoint
            self._send(200, str(len(EXPENSES)).encode())  # Returns expense items count
        else:  # Fallback for undefined routes
            self._send(404, b"not found")  # Returns 404 Not Found

    def _send(self, code, body):  # Helper method to build and send HTTP response
        self.send_response(code)  # Set HTTP status code (200, 404, etc.)
        self.send_header("Content-Type", "text/plain")  # Set response header type
        self.send_header("Content-Length", str(len(body)))  # Set response body length
        self.end_headers()  # End headers section
        self.wfile.write(body)  # Write response body to the output stream

    def log_message(self, *args):  # Suppress default server console log output
        pass


def make_server(port):  # Server factory function
    return HTTPServer(("0.0.0.0", port), Handler)  # Binds server to 0.0.0.0 on given port


if __name__ == "__main__":  # Main execution block
    port = int(os.environ.get("PORT", "8080"))  # Read $PORT variable or default to 8080
    make_server(port).serve_forever()  # Start the HTTP server listening loop
2. tests/test_server.py — Test Suite
Python
import os, sys, threading, unittest, urllib.request, urllib.error

# Import server factory from src directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from server import make_server


class TestService(unittest.TestCase):  # Test suite class inheriting from unittest
    @classmethod
    def setUpClass(cls):  # Class-level setup before running tests
        cls.srv = make_server(0)  # Bind server to a random available port (port 0)
        cls.port = cls.srv.server_address[1]  # Store the dynamically assigned port
        threading.Thread(
            target=cls.srv.serve_forever, daemon=True
        ).start()  # Run server in background thread

    @classmethod
    def tearDownClass(cls):  # Class-level teardown after all tests finish
        cls.srv.shutdown()  # Stop the background HTTP server

    def get(self, path):  # Helper method to perform HTTP GET requests to test server
        try:
            url = f"[http://127.0.0.1](http://127.0.0.1):{self.port}{path}"
            with urllib.request.urlopen(url) as r:
                return r.status, r.read().decode()  # Return status code and body text
        except urllib.error.HTTPError as e:
            return e.code, ""  # Catch HTTP errors and return error status code

    def test_root_answers(self):  # Test 1: Verify GET / returns HTTP 200
        self.assertEqual(self.get("/")[0], 200)

    def test_healthz_is_ok(self):  # Test 2: Verify GET /healthz returns HTTP 200 and body
        status, body = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertTrue(body.strip())

    def test_expenses_count(self):  # Test 3: Verify GET /expenses returns correct count
        self.assertEqual(self.get("/expenses")[1], "3")
How to run it
Start the service using the run script:   
JPG
Bash
./scripts/run.sh
How to test it
Execute the test suite using the test script[cite: 1]:
Bash
./scripts/test.sh
The script outputs a summary line matching TESTS: n/n[cite: 1].
Port configuration
Binds to interface 0.0.0.0[cite: 1].
Reads the PORT environment variable dynamically[cite: 1].
Defaults to port 8080 if PORT is not explicitly set[cite: 1].