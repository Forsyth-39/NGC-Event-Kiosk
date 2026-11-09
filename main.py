import sqlite3

# Connect to the database and define a cursor
def CreateEventsTable():
    try:
        conn = sqlite3.connect('')
        print("Database connected successfully") 
    except:
        print("Connection Failed")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
                   id INTEGER PRIMARY KEY,
                   company TEXT,
                   organiser_name TEXT,
                   room_number INTEGER,
                   capacity INTEGER
        )
""")
    
    cursor.execute(
        "INSERT INTO events (company, organiser_name, room_number, capacity) VALUES (?, ?, ?, ?)",
        ("Playstation", "James Olivier", 12, 500)
    )

    conn.commit()

    cursor.execute("SELECT sqlite_version()")

    result = cursor.fetchone()
    print(f"SQLITE version: {result[0]}")

    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


CreateEventsTable()