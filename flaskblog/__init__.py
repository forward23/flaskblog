import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '8e4d1af7db43352413620dc8f1de54cd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = os.environ.get('USER_EMAIL')
# app.config['MAIL_PASSWORD'] = os.environ.get('USER_PASS')
app.config['MAIL_USERNAME'] = 'ilia2307@gmail.com'
app.config['MAIL_PASSWORD'] = 'qsvfzetqlnwfsibr'
mail = Mail(app)

from flaskblog import routes