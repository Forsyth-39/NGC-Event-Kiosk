import mysql.connector

try:
    conn = mysql.connector.connect(
        host="s2344282.ncgrp.xyz",
        port=3306,
        user="Liam",
        password="nLJdJgd072BbkPJvnYmZ",
        database="KioskTest82",
    )
    # print("Connection successful")
except:
    print("Connection failed")
