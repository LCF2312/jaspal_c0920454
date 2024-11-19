# tests/test_db_write.py

import unittest
from pymongo import MongoClient

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        """Set up MongoDB connection"""
        self.client = MongoClient('mongodb://localhost:27017')  # Update with your MongoDB URI
        self.db = self.client['test_db']  # Replace with your database name
        self.collection = self.db['test_collection']

    def test_insert_document(self):
        """Test writing a document to MongoDB"""
        test_data = {"name": "Test User", "email": "test@example.com"}
        result = self.collection.insert_one(test_data)
        self.assertIsNotNone(result.inserted_id, "Document insertion failed.")

        # Verify the document exists
        query_result = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(query_result, "Inserted document not found in the database.")
        self.assertEqual(query_result['name'], "Test User")

if __name__ == '__main__':
    unittest.main()
