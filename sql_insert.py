import mysql.connector
import YOUR_PASSWORD

#store data in MySQL
def store():
    db1 = mysql.connector.connect(
        host='localhost', 
        user='root', 
        passwd=YOUR_PASSWORD.pw, 
        database='flashlight_scrape'
        )

    cur = db1.cursor()

    sql = """INSERT INTO cars 
    (market, brand, model, entity, engine, price, horsepower, bodystyle, serie, fuel, consumption, emission_co2, transmission, transmission_type, driveline, reaperstring, matchstring, datasource, datum)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    val = (market, brand, model, entity, engine, price, horsepower, bodystyle, serie, fuel, consumption, emission_co2, transmission, transmission_type, driveline, reaerstring, matchstring, datasource, datum)
    cur.execute(sql, val)

    db1.commit()
