from db_exten import database

class Student(database.Model):
    __tablename__ = "students"

    id = database.Column(database.Integer,primary_key = True)
    user_id = database.Column(database.Integer,database.ForeignKey("users.id"),nullable = False)
    roll_no = database.Column(database.String(10),nullable = False)
    batch = database.Column(database.String(10),nullable = False)
    cgpa = database.Column(database.Float,nullable = False)
    phone_no = database.Column(database.String(15),nullable = False,unique = True)
    is_blacklisted = database.Column(database.Boolean, default = False)
    is_placed = database.Column(database.Boolean, default = False)
    salary_placed = database.Column(database.String(10))

    placed_in = database.Column(database.Integer,database.ForeignKey("companies.id"))
    user = database.relationship("User", backref=database.backref("student", uselist=False))