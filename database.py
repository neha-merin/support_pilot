
import sqlite3

DATABASE_NAME = "tickets.db"


# ==========================================
# 1. DATABASE CONNECTION
# ==========================================

def get_connection():

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# 2. CREATE TICKETS TABLE
# ==========================================

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (

            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,

            employee_name TEXT NOT NULL,

            email TEXT NOT NULL,

            title TEXT NOT NULL,

            description TEXT NOT NULL,

            category TEXT,

            severity TEXT,

            business_impact TEXT,

            priority TEXT,

            confidence REAL,

            status TEXT DEFAULT 'Open',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()

    conn.close()

    print("Tickets table created successfully!")


# ==========================================
# 3. INSERT A NEW TICKET
# ==========================================

def save_ticket(
    employee_name,
    email,
    title,
    description,
    category,
    severity,
    business_impact,
    priority,
    confidence=None
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (
            employee_name,
            email,
            title,
            description,
            category,
            severity,
            business_impact,
            priority,
            confidence,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        employee_name,
        email,
        title,
        description,
        category,
        severity,
        business_impact,
        priority,
        confidence,
        "Open"
    ))

    ticket_id = cursor.lastrowid

    conn.commit()

    conn.close()

    return ticket_id


# ==========================================
# 4. RETRIEVE ALL TICKETS
# ==========================================

def get_all_tickets():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tickets
        ORDER BY created_at DESC
    """)

    tickets = cursor.fetchall()

    conn.close()

    return [dict(ticket) for ticket in tickets]


# ==========================================
# 5. RETRIEVE A TICKET BY ID
# ==========================================

def get_ticket_by_id(ticket_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tickets WHERE ticket_id = ?",
        (ticket_id,)
    )

    ticket = cursor.fetchone()

    conn.close()

    if ticket:
        return dict(ticket)

    return None


# ==========================================
# 6. TEST DATABASE
# ==========================================

if __name__ == "__main__":

    create_table()

    print("\nDatabase initialized successfully!")

