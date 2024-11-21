import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1', 
    user='sanjay',               
    password='StrongPass@123',          
    database='LiscensePlate'             
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM Owners')
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()

cursor.close()
connection.close()