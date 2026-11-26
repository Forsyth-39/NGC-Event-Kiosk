import mysql.connector, os, time, sys, random
from connection import conn
from login import login

seatNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

referenceNumber = login()
cursor = conn.cursor()

cursor.execute("SELECT 1 FROM Attendees WHERE booking_ref = %s", (referenceNumber,))
record_exists = cursor.fetchone() is not None

def Check_In():
    if record_exists:
        cursor.execute("SELECT has_attended FROM Attendees WHERE booking_ref = %s", (referenceNumber,))
        checkedIn = cursor.fetchone()
        checkedIn = checkedIn[0]
        checkedIn = str(checkedIn).strip()
        if str(checkedIn) == "1":
            print("Sorry, you have already checked in for this event")
        else:
            print("Would you like to check in?(y/n)")
            attended = input("> ")
            if attended.lower() == "y":
                print("You have checked in!")
                print(f"Your seat number is: {random.choice(seatNumbers)}")
                sql = "UPDATE Attendees SET has_attended = %s WHERE has_attended = %s AND booking_ref = %s"
                # Execute the update with parameters (prevents SQL injection)
                cursor.execute(sql, (1, 0, referenceNumber))
                conn.commit()
                cursor.close()
                conn.close()
                exit()
            else:
                print("If you want to check in for a different event, please restart and enter a new booking reference!")
                time.sleep(1)
                exit()
    else:
        print("Sorry, the reference number you inputted cannot be found, you can try again or check if you have booked any events")

Check_In()

cursor.close()
conn.close()
