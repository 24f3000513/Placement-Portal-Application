from flask import *
from flask_login import login_user,logout_user,login_required
from models import User

auth_bp = Blueprint("auth",__name__)

@auth_bp.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pasw = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.chk_hash_pasw(pasw):
            login_user(user)

            if user.roles == 'admin':
                return redirect(url_for('admin'))
            elif user.roles == 'student':
                return redirect(url_for('student'))
            elif user.roles == 'company':
                return redirect(url_for('company'))
        else:
            return "Invalid Credentials"
    else:
        return render_template('login.html')

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html')