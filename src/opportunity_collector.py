import requests

from opportunity import Opportunity
from bs4 import BeautifulSoup


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
    job_type = [job_type.lower() for job_type in job["jobType"]]

    if "intern" in job_title:
        return True

    if "internship" in job_type:
        return True

    return False