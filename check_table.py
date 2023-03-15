import connect_db

connect_db.mycursor.execute("SHOW columns FROM cars")
print([column[0] for column in connect_db.mycursor.fetchall()])

connect_db.mycursor.execute("SELECT * FROM cars")
result = connect_db.mycursor.fetchall()
for row in result:
    print(row)
    print("\n")
