from db_exten import database
from sqlalchemy import Enum

class Drive(database.Model):
    __tablename__ = "drives"

    id = database.Column(database.Integer, primary_key=True)
    c_id = database.Column(database.Integer, database.ForeignKey("companies.id"), nullable=False)

    job_title = database.Column(database.String(100))
    job_description = database.Column(database.Text)
    salary_min = database.Column(database.Float)
    salary_max = database.Column(database.Float)
    eligibility = database.Column(database.Text)
    deadline = database.Column(database.Date)

    status = database.Column(Enum("pending", "approved", "rejected", name="drive_status"),default="pending")
    company = database.relationship("Company", backref="drives")
    