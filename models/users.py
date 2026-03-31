from db_exten import database
from sqlalchemy import Enum
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash,check_password_hash

class User(UserMixin,database.Model):
    __tablename__ = "users"

    id = database.Column(database.Integer,primary_key = True)
    name = database.Column(database.String(50),nullable = False)
    email = database.Column(database.String(50),nullable = False,unique = False)
    password = database.Column(database.Text,nullable = False)

    roles = database.Column(Enum("student", "company", "admin", name="user_role"),nullable = False)
    is_active = database.Column(database.Boolean, default=True)

    def valid_pasw(self, pasw):
        if len(pasw) < 8:
            return False, "Password must be more than 7 characters"

        if not any(c.isupper() for c in pasw):
            return False, "Password must contain at least one uppercase letter"

        if not any(c.islower() for c in pasw):
            return False, "Password must contain at least one lowercase letter"

        if not any(c in "!@#$%^&*[](){}" for c in pasw):
            return False, "Password must contain at least one special character (!@#$%^&*[](){})"

        return True, "Valid password"
    
    def pasw_hash(self,pasw):
        x,msg = self.valid_pasw(pasw)
        if x :
            self.password = generate_password_hash(pasw)
            return True,msg
        else:
            return False,msg

    def chk_hash_pasw(self,pasw):
        return check_password_hash(self.password,pasw)


