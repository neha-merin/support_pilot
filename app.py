
from flask import Flask, request, jsonify, render_template

from classifier import process_ticket
from database import (
    create_table,
    save_ticket,
    get_all_tickets,
    get_ticket_by_id
)

# ==========================================
# 1. INITIALIZE FLASK APPLICATION
# ==========================================

app = Flask(__name__)

# Create database table when application starts
create_table()


# ==========================================
# 2. HOME ROUTE
# ==========================================

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# ==========================================
# 3. SUBMIT AND PROCESS TICKET
# ==========================================

@app.route("/ticket", methods=["POST"])
def create_ticket():

    # Accept JSON or HTML form data
    data = request.get_json(silent=True)

    if data is None:
        data = request.form

    # Extract employee details
    employee_name = data.get("employee_name", "").strip()
    email = data.get("email", "").strip()
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()

    # Validate required fields
    if not all([employee_name, email, title, description]):

        return jsonify({
            "error": "All fields are required"
        }), 400

    try:

        # AI ticket processing
        result = process_ticket(description)

        category = result["category"]
        severity = result["severity"]
        business_impact = result["business_impact"]
        priority = result["priority"]

        # Save ticket in SQLite
        ticket_id = save_ticket(
            employee_name=employee_name,
            email=email,
            title=title,
            description=description,
            category=category,
            severity=severity,
            business_impact=business_impact,
            priority=priority
        )

        # Send response
        return jsonify({

            "message": "Ticket submitted successfully",

            "ticket_id": ticket_id,

            "employee_name": employee_name,

            "title": title,

            "description": description,

            "category": category,

            "severity": severity,

            "business_impact": business_impact,

            "priority": priority,

            "status": "Open"

        }), 201

    except FileNotFoundError:

        return jsonify({
            "error": "Trained classification model not found. Train the model first."
        }), 500

    except Exception as e:

        app.logger.exception("Ticket processing failed")

        return jsonify({
            "error": "Unable to process ticket"
        }), 500


# ==========================================
# 4. GET ALL TICKETS
# ==========================================

@app.route("/tickets", methods=["GET"])
def view_tickets():

    tickets = get_all_tickets()

    return jsonify({

        "total_tickets": len(tickets),

        "tickets": tickets

    })


# ==========================================
# 5. GET TICKET BY ID
# ==========================================

@app.route("/ticket/<int:ticket_id>", methods=["GET"])
def view_ticket(ticket_id):

    ticket = get_ticket_by_id(ticket_id)

    if ticket is None:

        return jsonify({
            "error": "Ticket not found"
        }), 404

    return jsonify(ticket)


# ==========================================
# 6. RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
