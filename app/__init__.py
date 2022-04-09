from flask import Flask
from flask_mail import Message, Mail
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
import os

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect(app)

# Load the views
from app import views

#Flask-Mail initialization
mail = Mail()

# Load the config file
app.config.from_object('config')
app.secret_key = 'ldCz3GWmhos8QUJPGVt9'

#mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv('EMAIL_USER')
app.config["MAIL_PASSWORD"] = os.getenv('EMAIL_PASSWORD')
mail.init_app(app)

bootstrap = Bootstrap(app)