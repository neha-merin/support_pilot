
import joblib


# ==========================================
# 1. LOAD TRAINED ML MODEL
# ==========================================

MODEL_PATH = "models/ticket_classifier.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


# ==========================================
# 2. SEVERITY PREDICTION
# ==========================================

def predict_severity(ticket):

    text = ticket.lower()

    critical_words = [
        "server down",
        "entire company",
        "production down",
        "security breach",
        "system outage",
        "all users affected",
        "entire production server"
    ]

    high_words = [
        "urgent",
        "cannot work",
        "business stopped",
        "client meeting",
        "vpn not working",
        "unable to work",
        "business operations affected"
    ]

    medium_words = [
        "slow",
        "error",
        "problem",
        "issue",
        "frequently disconnecting"
    ]

    # Check critical severity
    for word in critical_words:
        if word in text:
            return "Critical"

    # Check high severity
    for word in high_words:
        if word in text:
            return "High"

    # Check medium severity
    for word in medium_words:
        if word in text:
            return "Medium"

    # Default severity
    return "Low"


# ==========================================
# 3. BUSINESS IMPACT PREDICTION
# ==========================================

def predict_business_impact(ticket):

    text = ticket.lower()

    high_impact_words = [
        "entire company",
        "production",
        "client meeting",
        "business stopped",
        "cannot work",
        "all users",
        "business operations"
    ]

    for word in high_impact_words:
        if word in text:
            return "High"

    return "Low"


# ==========================================
# 4. PRIORITY CALCULATION
# ==========================================

def calculate_priority(severity, business_impact):

    if severity == "Critical":
        return "P1"

    elif severity == "High" and business_impact == "High":
        return "P1"

    elif severity == "High":
        return "P2"

    elif severity == "Medium":
        return "P3"

    else:
        return "P4"


# ==========================================
# 5. COMPLETE TICKET PROCESSING
# ==========================================

def process_ticket(ticket):

    # Load trained classification model
    model = load_model()

    # Predict ticket category
    category = model.predict([ticket])[0]

    # Predict severity
    severity = predict_severity(ticket)

    # Predict business impact
    business_impact = predict_business_impact(ticket)

    # Calculate priority
    priority = calculate_priority(
        severity,
        business_impact
    )

    # Return all predictions
    return {
        "category": category,
        "severity": severity,
        "business_impact": business_impact,
        "priority": priority
    }


# ==========================================
# 6. TESTING
# ==========================================

if __name__ == "__main__":

    tickets = [
        "I forgot my company password",

        "My WiFi is very slow",

        "VPN is not working and I cannot work. "
        "I have a client meeting",

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
