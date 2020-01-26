import unittest
from local_events import app
import app as project
from local_events import routes
import os
from flask import url_for, session

class testApp(unittest.TestCase):

    """Set up and tear down"""
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = project.app.test_client()
 
        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
    
    """
    Test suite for app.py
    """
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)

    def test_env_variables(self):
        database_url = os.getenv("MONGO_URI")
        self.assertEqual(database_url, os.getenv("MONGO_URI"))
        database_name = os.getenv("MONGO_DBNAME")
        self.assertEqual(database_name, os.getenv("MONGO_DBNAME"))
        secret_key = os.getenv("SECRET_KEY")
        self.assertEqual(secret_key, os.getenv("SECRET_KEY"))
    
    def test_database_name_matches_database_url(self):
        database_url = os.getenv("MONGO_URI")
        database_name = os.getenv("MONGO_DBNAME")
        self.assertIn(database_name, database_url)

    def test_collections(self):
        self.assertIsNotNone(venues_collection)
        self.assertIsNotNone(bands_collection)

    def test_main_page(self):
        response1 = self.app.get('/')
        response2 = self.app.get('/a')
        self.assertEqual(response1.status_code, 200)
        self.assertNotEqual(response2.status_code, 200)

if __name__ == "__main__":
    unittest.main()  