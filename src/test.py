from opportunity_collector import collect_internships, save_opportunities
from functions import get_internships


opportunities = collect_internships()

print("Internships found:", len(opportunities))

save_opportunities(opportunities)

internships = get_internships()

print("\nDatabase records:", len(internships))

for internship in internships:
    print("\nID:", internship.id)
    print("Company:", internship.company)
    print("Role:", internship.role)
    print("Description saved:", bool(internship.description))