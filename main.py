import sqlite3 
conn = sqlite3.connect('sql.db') 
cursor = conn.cursor() 
 
# Executes a query to get the sqlite version 
query = 'SELECT sqlite_version();' 
cursor.execute(query) 

#Fetch and print the results 
result = cursor.fetchall() 
print(f'SQLite Version is {result[0][0]}') 
