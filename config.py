import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'devkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///callcenter.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = 'your_account_sid_here'
    TWILIO_AUTH_TOKEN = 'your_auth_token_here'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number_here'
