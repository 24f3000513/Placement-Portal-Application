from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import *
from flask_bcrypt import check_password_hash,generate_password_hash
from config import *
from db_exten import database
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,InputRequired,ValidationError
from routes.auth import auth_bp
from models import User
import os


l_manager = LoginManager()
l_manager.login_view = "auth.login"

app = Flask(__name__)
app.config.from_object(Config)

database.init_app(app)
l_manager.init_app(app)

app.register_blueprint(auth_bp)

os.makedirs('database',exist_ok=True)

with app.app_context():
    from models import User, Student, Company, Drive, Application
    database.create_all()

    try:
        chk_admin = User.query.filter_by(roles="admin", email="admin@cistm.ac.in").first()
        if not chk_admin:
            admin = User(name="Admin",
                        email="admin@cistm.ac.in",
                        roles="admin")
            admin.pasw_hash("Admin@123")
            database.session.add(admin)
            database.session.commit()
            print("Admin created successfully")
    except Exception as e:
        print(f"Error: {e}")

@app.route("/", methods = ['GET','POST'])
def home():
    return redirect(url_for('auth.login'))


@l_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods = ['GET','POST'])
def register():
    return render_template('register.html')


@app.route("/admin/dashboard")
@login_required
def admin():
    if current_user.roles != "admin":
        return "Unauthorized", 403
    return render_template('admin.html')


@app.route("/student/dashboard")
@login_required
def student():
    if current_user.roles != "student":
        return "Unauthorized", 403 
    return render_template('student.html')


@app.route("/company/dashboard")
@login_required
def company():
    if current_user.roles != "company":
        return "Unauthorized", 403 
    return render_template('company.html')


if __name__ == "__main__":
    app.run(debug=True)