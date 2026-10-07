from datetime import date

from database import SessionLocal
from models import Internship


def add_internship(
    company,
    role,
    location,
    url,
    deadline=None,
    skills=None,
    status="Not Applied",
    resume_used=None,
    notes=None
):
    db = SessionLocal()
    existing = db.query(Internship).filter(
        Internship.url == url
    ).first()

    if existing:
        db.close()
        return existing

    internship = Internship(
        company=company,
        role=role,
        location=location,
        url=url,
        deadline=deadline,
        skills=skills,
        status=status,
        date_found=date.today(),
        resume_used=resume_used,
        notes=notes
    )

    db.add(internship)
    db.commit()
    db.refresh(internship)

    db.close()

    return internship

def get_internships():
    db = SessionLocal()

    internships = db.query(Internship).all()

    db.close()

    return internships

def get_internship(internship_id):
    db = SessionLocal()

    internship = db.query(Internship).filter(
        Internship.id == internship_id
    ).first()

    db.close()

    return internship

def update_internship(internship_id, **updates):
    db = SessionLocal()

    internship = db.query(Internship).filter(
        Internship.id == internship_id
    ).first()

    if internship:
        for field, value in updates.items():
            if hasattr(internship, field):
                setattr(internship, field, value)

        db.commit()
        db.refresh(internship)

    db.close()

    return internship

def delete_internship(internship_id):
    db = SessionLocal()

    internship = db.query(Internship).filter(
        Internship.id == internship_id
    ).first()

    if internship:
        db.delete(internship)
        db.commit()

        result = True
    else:
        result = False

    db.close()

    return result

def job_to_opportunity(job):
    return Opportunity(
        company=job["companyName"],
        role=job["jobTitle"],
        location=job["jobGeo"],
        url=job["url"],
        skills=None
    )

def is_internship(job):
    job_title = job["jobTitle"].lower()
    job_type = [job_type.lower() for job_type in job["jobType"]]

    if "intern" in job_title:
        return True

    if "internship" in job_type:
        return True

    return False