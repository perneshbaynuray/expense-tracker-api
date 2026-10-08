import os
import sys
import json
import threading
import unittest
import urllib.request
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from server import make_server


class TestExpenseTracker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def get(self, path):
        try:
            url = f"http://127.0.0.1:{self.port}{path}"
            with urllib.request.urlopen(url) as response:
                return response.status, response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            return error.code, ""

    def test_root_answers_200(self):
        status, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn("Expense Tracker API", body)

    def test_healthz_is_ok(self):
        status, body = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(body.strip(), "ok")

    def test_expenses_returns_data(self):
        status, body = self.get("/expenses")
        self.assertEqual(status, 200)
        data = json.loads(body)
        self.assertEqual(len(data), 100)


if __name__ == "__main__":
    unittest.main()
  