import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',  
    user='sanjay',
    password='StrongPass@123',
    database='LiscensePlate'
)

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Owners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phNo VARCHAR(255) UNIQUE NOT NULL,
    altPhNo VARCHAR(255) UNIQUE NOT NULL,
    liscensePlateNo VARCHAR(255) UNIQUE NOT NULL
)
''')

cursor.execute('''
INSERT INTO Owners (name, age, email, phNo, altPhNo, liscensePlateNo)
VALUES (%s, %s, %s, %s, %s, %s)
''', ('Rangesh', 21, 'Rangesh@gmail.com', '9897698976', '8987689876', 'MH12DE1433'))

connection.commit()

cursor.close()
connection.close()