import mysql.connector, os, sys, time
from connection import conn

def login():
    print("Enter your Booking Reference number:")
    bookingReference = input("> ")
    referenceLength = len(bookingReference)
    firstThreeCharacters = bookingReference[:3]
    if referenceLength > 8 or referenceLength < 8:
        print("Invalid reference number. The reference number is 8 Characters long")
        exit()
    if not firstThreeCharacters.isalpha():
        print("The first three characters of the reference number need to be letters")
        exit()
    return bookingReference

referenceNumber = login()
