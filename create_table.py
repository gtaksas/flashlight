import mysql.connector
import YOUR_PASSWORD

db1 = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=YOUR_PASSWORD.pw,
    database='flashlight_scrape'
)

mycursor = db1.cursor()

mycursor.execute("""CREATE TABLE cars 
(id int PRIMARY KEY AUTO_INCREMENT)
""")

mycursor.execute("""ALTER TABLE cars ADD
(market VARCHAR(20), brand VARCHAR(20), model VARCHAR(20), entity VARCHAR(20), engine VARCHAR(20), price int, horsepower VARCHAR(20), bodystyle VARCHAR(20), serie VARCHAR(20), fuel VARCHAR(20), consumption VARCHAR(20), emission_co2 VARCHAR(20), transmission VARCHAR(20), transmission_type VARCHAR(20), driveline VARCHAR(20), reaperstring VARCHAR(20), matchstring VARCHAR(20), datasource VARCHAR(40), datum VARCHAR(20))
""")


mycursor.execute("DESCRIBE cars")

for i in mycursor:
    print(i)
