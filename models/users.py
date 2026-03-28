from db_exten import database
from sqlalchemy import Enum
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash,check_password_hash

class User(database.Model):
    __tablename__ = "users"

    id = database.Column(database.Integer,primary_key = True)
    name = database.Column(database.String(50),nullable = False)
    email = database.Column(database.String(50),nullable = False,unique = False)
    password = database.Column(database.Text,nullable = False)

    roles = database.Column(Enum("student", "company", "admin", name="user_role"),nullable = False)
    is_active = database.Column(database.Boolean, default=True)

    def pasw_hash(self,pasw):
        self.password = generate_password_hash(pasw)

    def chk_hash_pasw(self,pasw):
        return check_password_hash(self.password,pasw)


