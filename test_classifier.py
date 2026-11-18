
from classifier import (
    predict_severity,
    predict_business_impact,
    calculate_priority,
    process_ticket
)

tickets = [
    "I forgot my company password",

    "My WiFi is very slow",

    "VPN is not working and I cannot work. I have a client meeting",

    "Entire production server is down"
]

for ticket in tickets:

    result = process_ticket(ticket)

    print("\nTicket:", ticket)
    print("Category:", result["category"])
    print("Severity:", result["severity"])
    print("Business Impact:", result["business_impact"])
    print("Priority:", result["priority"])
    print("-" * 50)
