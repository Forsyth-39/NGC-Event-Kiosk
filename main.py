import sqlite3

# Connect to the database and define a cursor
def CreateMembersTable():
    try:
        conn = sqlite3.connect('')
        print("Database connected successfully") 
    except:
        print("Connection Failed")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   email TEXT,
                   reference_number TEXT
        )
""")
    
    cursor.execute(
        "INSERT INTO members (name, email, reference_number) VALUES (?, ?, ?)",
        ("Liam", "testuser@gmail.com", "LF1234567")
    )

    conn.commit()

    cursor.execute("SELECT sqlite_version()")

    result = cursor.fetchone()
    print(f"SQLITE version: {result[0]}")

    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    LogIn(conn)

def LogIn(conn):
    cursor = conn.cursor()

    print("Enter your name")
    name = input("> ")

    print("Enter your reference number:")
    urn = input("> ")

    cursor.execute(f"""SELECT reference_number FROM members 
                   WHERE {name} == name """)
    
    result = cursor.fetchone()

    if result == urn:
        print("User found")
    else:
        print("You entered an incorrect reference number")
    

CreateMembersTable()