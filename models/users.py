from db_exten import database
from sqlalchemy import Enum

class User(database.Model):
    __tablename__ = "users"

    id = database.Column(database.Integer,primary_key = True)
    name = database.Column(database.String(50),nullable = False)
    email = database.Column(database.String(50),nullable = False,unique = False)
    password = database.Column(database.Text,nullable = False)

    roles = database.Column(Enum("student", "company", "admin", name="user_role"),nullable = False)
    is_active = database.Column(database.Boolean, default=True)


