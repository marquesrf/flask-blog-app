import os

class Config:
    SECRET_KEY = 'i-(s5X)]jxVpR&qGfLqT.2Tvnapg'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myblog.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')