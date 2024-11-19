# tests/test_db_read.py

import unittest
from pymongo import MongoClient

class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        """Set up MongoDB connection"""
        self.client = MongoClient('mongodb://localhost:27017')  # Update with your MongoDB URI
        self.db = self.client['test_db']  # Replace with your database name

    def test_db_connection(self):
        """Test MongoDB connection using ping"""
        try:
            self.client.admin.command('ping')
            connected = True
        except Exception as e:
            connected = False
        self.assertTrue(connected, "Database connection failed.")

if __name__ == '__main__':
    unittest.main()
