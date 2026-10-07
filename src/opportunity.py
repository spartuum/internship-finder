from dataclasses import dataclass
from datetime import date


@dataclass
class Opportunity:
    company: str
    role: str
    location: str
    url: str
    deadline: date | None = None
    skills: str | None = None
    description: str | None = None