
from database import create_table, save_ticket, get_all_tickets

# Create table
create_table()

# Insert sample ticket
ticket_id = save_ticket(
    employee_name="Arun",
    email="arun@company.com",
    title="VPN not working",
    description="Unable to connect to company VPN",
    category="VPN",
    severity="High",
    business_impact="High",
    priority="P1"
)

print("Ticket saved successfully!")
print("Ticket ID:", ticket_id)

# Retrieve stored tickets
tickets = get_all_tickets()

print("\nStored Tickets:")

for ticket in tickets:
    print(ticket)
