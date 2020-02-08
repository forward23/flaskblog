import os



class Config:
    SECRET_KEY = '8e4d1af7db43352413620dc8f1de54cd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('USER_EMAIL')
    MAIL_PASSWORD = os.environ.get('USER_PASS')