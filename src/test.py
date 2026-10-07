import requests

from opportunity_collector import is_internship


url = "https://jobicy.com/api/v2/remote-jobs"

response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()
jobs = data["jobs"]

internships = []

for job in jobs:
    if is_internship(job):
        internships.append(job)

print("Total jobs:", len(jobs))
print("Possible internships:", len(internships))

print("\nInternships found:")

for job in internships:
    print("------------------------")
    print("Title:", job["jobTitle"])
    print("Company:", job["companyName"])
    print("Location:", job["jobGeo"])