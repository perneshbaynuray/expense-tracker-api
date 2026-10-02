
import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

EXPENSES = [
    {"id": 1, "title": "Coffee", "amount": 4.50, "category": "Food"},
    {"id": 2, "title": "Subway ticket", "amount": 2.00, "category": "Transport"},
    {"id": 3, "title": "Books", "amount": 25.00, "category": "Education"}
]

class ExpenseTrackerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self._send_response(200, "text/plain", "ok")
        elif self.path == "/":
            self._send_response(200, "application/json", json.dumps({"message": "Expense Tracker API is running"}))
        elif self.path == "/expenses":
            self._send_response(200, "application/json", json.dumps(EXPENSES))
        else:
            self._send_response(404, "text/plain", "not found")

    def _send_response(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        encoded_body = body.encode("utf-8")
        self.send_header("Content-Length", str(len(encoded_body)))
        self.end_headers()
        self.wfile.write(encoded_body)

    def log_message(self, format, *args):
        pass

def make_server(port):
    return HTTPServer(("0.0.0.0", port), ExpenseTrackerHandler)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    server = make_server(port)
    server.serve_forever()

       

