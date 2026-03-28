from flask import *
from flask_login import login_user,logout_user,login_required
from models import User

auth_bp = Blueprint("auth",__name__)
