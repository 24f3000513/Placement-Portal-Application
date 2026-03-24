import os

DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "Kousthubh2304"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DIR, "database", "placementportal.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False