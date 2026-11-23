import mysql.connector, os, time, sys
from connection import conn
from login import login

referenceNumber = login()
cursor = conn.cursor()

cursor.execute("SELECT 1 FROM Attendees WHERE booking_ref = %s", (referenceNumber,))
record_exists = cursor.fetchone() is not None

if record_exists:
    cursor.execute("SELECT has_attended FROM Attendees WHERE booking_ref = %s", (referenceNumber,))
    checkedIn = cursor.fetchone()
    print(checkedIn)
    if checkedIn != 0:
        print("Sorry, you have already checked in for this event")
    else:
        print("Would you like to check in?(y/n)")
        attended = input("> ")
        if attended.lower() == "y":
            print("You have checked in!")
            sql = "UPDATE Attendees SET has_attended = %s WHERE booking_ref = %s"
            values = (True, referenceNumber)  # (new_value, old_value)
            # Execute the query
            cursor.execute(sql, values)
            exit()
        else:
            print("If you want to check in for a different event, please restart and enter a new booking reference!")
            time.sleep(1)
            exit()
else:
    print("Sorry, the reference number you inputted cannot be found, you can try again or check if you have booked any events")

cursor.close()
conn.close()
