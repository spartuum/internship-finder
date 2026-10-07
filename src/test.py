from opportunity_collector import collect_internships, save_opportunities
from functions import get_internships


opportunities = collect_internships()

print("Internships found:", len(opportunities))

save_opportunities(opportunities)

internships = get_internships()

print("\nDatabase records:", len(internships))

for internship in internships:
    print("\nCompany:", internship.company)
    print("Role:", internship.role)
    print("Industry:", internship.industry)
    print("Level:", internship.level)
    print("Type:", internship.job_type)
    print("Published:", internship.published_at)