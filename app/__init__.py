from flask import Flask
from config import Config
from flask_mail import Mail

application = Flask(__name__)
application.config.from_object(Config)
application.config.from_pyfile('config.cfg')

mail = Mail(application)

from app import routes
