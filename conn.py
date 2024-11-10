import mysql.connector


class conn:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="carparking_python"
    )

    mycursor = mydb.cursor()
