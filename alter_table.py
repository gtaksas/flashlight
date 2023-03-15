import connect_db

#connect_db.mycursor.execute("ALTER TABLE cars RENAME COLUMN reaerstring TO reaperstring;")
#connect_db.mycursor.execute("ALTER TABLE cars CHANGE price price CHAR(30);")
#connect_db.mycursor.execute("ALTER TABLE cars CHANGE reaperstring reaperstring CHAR(100);")
connect_db.mycursor.execute("ALTER TABLE cars CHANGE matchstring matchstring CHAR(100);")
connect_db.mycursor.execute("ALTER TABLE cars CHANGE datum datum VARCHAR(50);")

connect_db.mycursor.execute("SHOW columns FROM cars")
print([column[0] for column in connect_db.mycursor.fetchall()])

connect_db.db1.close()