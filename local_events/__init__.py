from flask import Flask
from flask_pymongo import PyMongo
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'local_events'
app.config["MONGO_URI"] = 'mongodb+srv://root:eu4QBwmtZMzd0HU6@myfirstcluster-xm8rq.mongodb.net/test?retryWrites=true&w=majority'
# this solves CSRF key issues
app.config['SECRET_KEY'] = '5cb1e06f07b9f75dd34cb6ea90649d18'

mongo = PyMongo(app)
csrf = CSRFProtect(app)

from local_events import routes