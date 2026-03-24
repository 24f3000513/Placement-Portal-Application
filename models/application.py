from db_exten import database
from sqlalchemy import Enum

class Application(database.Model):
    __tablename__ = "applications"

    id = database.Column(database.Integer, primary_key=True)

    student_id = database.Column(database.Integer, database.ForeignKey("students.id"), nullable=False)
    drive_id = database.Column(database.Integer, database.ForeignKey("drives.id"), nullable=False)

    status = database.Column(Enum("applied", "shortlisted", "rejected", "selected", name="application_status"),default="applied")

    student = database.relationship("Student", backref="applications")
    drive = database.relationship("Drive", backref="applications")

    __table_args__ = (database.UniqueConstraint("student_id", "drive_id", name="application"),)
    