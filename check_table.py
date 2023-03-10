import mysql.connector
import YOUR_PASSWORD

db1 = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=YOUR_PASSWORD.pw,
    database='flashlight_scrape'
)

mycursor = db1.cursor()


mycursor.execute("SELECT * FROM cars")
result = mycursor.fetchall()
for row in result:
    print(row)
    print("\n")
