from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import *
from flask_bcrypt import check_password_hash,generate_password_hash
from config import *
from db_exten import database
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,InputRequired,ValidationError
from routes.auth import auth_bp
import os


login_manager = LoginManager()
login_manager.login_view = "auth.login"


app = Flask(__name__)
app.config.from_object(Config)

database.init_app(app)
login_manager.init_app(app)

os.makedirs('database',exist_ok=True)

with app.app_context():
    from models import User,Student,Company,Drive,Application

    database.create_all()

@app.route("/", methods = ['GET','POST'])
def home():
    return render_template('login.html')

from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pasw = request.form['pasw']

        user = User.query.filter_by(email=email).first()

        if user and user.chk_hash_pasw(pasw):
            login(user)

        if user.role == 'admin':
            return render_template(url_for('admin_db'))
        elif user.role == 'student':
            return render_template(url_for('student_db'))
        elif user.role == 'company':
            return render_template(url_for('company_db'))
        else:
            return "Invalid Credentials"
        
    else:
        return render_template('login.html')

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html')

@app.route("/register", methods = ['GET','POST'])
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)