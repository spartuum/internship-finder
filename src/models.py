from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Internship(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, autoincrement=True)

    company = Column(String(100), nullable=False)
    role = Column(String(200), nullable=False)
    location = Column(String(200))

    url = Column(Text, nullable=False)
    deadline = Column(Date)

    skills = Column(Text)

    status = Column(String(50), default="Not Applied")

    date_found = Column(Date)

    resume_used = Column(String(200))

    notes = Column(Text)