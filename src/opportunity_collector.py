import requests

from opportunity import Opportunity
from bs4 import BeautifulSoup
import re

API_URL = "https://jobicy.com/api/v2/remote-jobs"


def fetch_jobs():
    response = requests.get(API_URL, timeout=30)

    response.raise_for_status()

    return response.json()["jobs"]


def create_opportunity(
    company,
    role,
    location,
    url,
    deadline=None,
    skills=None
):
    return Opportunity(
        company=company,
        role=role,
        location=location,
        url=url,
        deadline=deadline,
        skills=skills
    )


def fetch_url(url):
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.text

import requests
from bs4 import BeautifulSoup

from opportunity import Opportunity


def create_opportunity(
    company,
    role,
    location,
    url,
    deadline=None,
    skills=None
):
    return Opportunity(
        company=company,
        role=role,
        location=location,
        url=url,
        deadline=deadline,
        skills=skills
    )


def fetch_url(url):
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.text


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title

    if title:
        print("Page title:", title.get_text(strip=True))

    links = soup.find_all("a")

    print("Number of links:", len(links))

    for link in links:
        print("Link:", link.get("href"))

    return soup


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

    if re.search(r"\bintern(ship)?\b", job_title):
        return True

    for job_type in job["jobType"]:
        if job_type.lower() == "internship":
            return True

    return False

def collect_internships():
    jobs = fetch_jobs()
    opportunities = []

    for job in jobs:
        if is_internship(job):
            opportunities.append(job_to_opportunity(job))

    return opportunities

from functions import add_internship


def save_opportunities(opportunities):
    for opportunity in opportunities:
        add_internship(
            company=opportunity.company,
            role=opportunity.role,
            location=opportunity.location,
            url=opportunity.url,
            deadline=opportunity.deadline,
            skills=opportunity.skills
        )