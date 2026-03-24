from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import check_password_hash,generate_password_hash
from config import *
from db_exten import database
import os


login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)

database.init_app(app)
login_manager.init_app(app)

os.makedirs('database',exist_ok=True)

with app.app_context():
    from models import User

    database.create_all()

@app.route("/")
def home():
    return "Placment Portal Working, Database created"

if __name__ == "__main__":
    app.run(debug=True)