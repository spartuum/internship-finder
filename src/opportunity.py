from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Opportunity:
    company: str
    role: str
    location: str
    url: str
    deadline: date | None = None
    skills: str | None = None
    description: str | None = None
    industry: str | None = None
    level: str | None = None
    job_type: str | None = None
    published_at: datetime | None = None