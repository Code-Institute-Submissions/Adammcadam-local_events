import unittest
import re
import app as app_module

from flask_pymongo import PyMongo

app + app_module.app

# setting up test DB on MongoDB and switching off CSRF checks

app.config["TESTING"] = true
app.config["WTF_CSRF_ENABLED"] = false
app.config["MONGO_URI"] = 'mongodb+srv://root:eu4QBwmtZMzd0HU6@myfirstcluster-xm8rq.mongodb.net/local_events_test?retryWrites=true&w=majority'

mongo = PyMongo(app)
app_module.mongo = mongo

class AppTestCase(unittest.TestCase):
    def setup(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.bands.delete_many({})
            mongo.db.venues.delete_many({})
            
            
class AppTests(AppTestCase):
    def test_index(self):
        result = self.client.get('/')
        data = result.data.decode('utf-8')
        assert result.status =='200 OK'
        assert 'Local Events' in data
        
    def test_bands(self):
        result = self.client.get('/get_bands')
        data = result.data.decode('utf-8')
        assert result.status =='200 OK'
        assert 'bands' in data
        
    def test_venues(self):
        result = self.client.get('/get_venues')
        data = result.data.decode('utf-8')
        assert result.status =='200 OK'
        assert 'venues' in data
        
    def test_band_create(self):
        result = self.client.post('/insert_band', follow_redirects=True, data={
            'band_name' : 'test',
            'event_date' : '11/29/2019 10:00',
            'venue_name' : 'test',
            'is_headlining' : False,
            'views' : 0,
            'is_done' : False
        })
        data = result.data.decode('utf-8')
        assert 'band' in data
        
    def test_venue_create(self):
        result = self.client.post('/insert_band', follow_redirects=True, data={
            'venue_name' : 'test',
            'venue_desc' : 'testing test',
            'venue_location' : 'test',
            'venue_website' : 'testing.com'
        })
        data = result.data.decode('utf-8')
        assert 'venue' in data

