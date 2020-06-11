from django.http import HttpResponse
import MySQLdb


def index(request):
    print("Connecting to database using MySQLdb")
    db_connection = MySQLdb.connect(host='localhost',
                                    db='holiday',
                                    user='root',
                                    passwd='adminpass1',
                                    port=3307)
    message = "\nSuccesfully Connected to database using MySQLdb!"

    query = "SELECT * FROM attractions"
    cursor = db_connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    for row in records:
        message += '\n'
        for e in row:
            message += str(e) + " "

    db_connection.close()
    return HttpResponse("Hello, world. You're at the polls index." + message)
