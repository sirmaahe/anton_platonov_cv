from flask import Flask
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.secret_key = 'SECRET KEY'
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app)

from app import views
