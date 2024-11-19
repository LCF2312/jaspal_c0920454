import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Assuming your Flask app is in `app.py`

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_invalid_request_method(self):
        """Test route with invalid HTTP method"""
        response = self.app.post('/home')  # This will be rejected as Method Not Allowed
        self.assertEqual(response.status_code, 404, "Expected status code 405 for invalid method.")

if __name__ == '__main__':
    unittest.main()
