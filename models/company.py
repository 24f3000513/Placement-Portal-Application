from db_exten import database

class Company(database.Model):
    __tablename__ = "companies"

    id = database.Column(database.Integer,primary_key = True)
    user_id = database.Column(database.Integer,database.ForeignKey("users.id"),nullable = False)

    company_name = database.Column(database.String(50),nullable = False)
    hr_contact = database.Column(database.String(30),nullable = False)
    location = database.Column(database.String(100),nullable = False)
    website = database.Column(database.String(100))

    is_blacklisted = database.Column(database.Boolean, default = False)
    is_approved = database.Column(database.Boolean, default = False)

    user = database.relationship("User", backref=database.backref("company", uselist=False))