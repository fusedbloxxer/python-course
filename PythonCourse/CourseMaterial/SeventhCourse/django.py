import MySQLdb
print("Connecting to database using MySQLdb")
db_connection = MySQLdb.connect(host='localhost',
								db='holiday',
								user='root',
								passwd='adminpass1',
                                port=3307)
print("Succesfully Connected to database using MySQLdb!")
db_connection.close()