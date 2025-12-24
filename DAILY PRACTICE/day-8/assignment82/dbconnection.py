import mysql.connector


def getconnection():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "home_appliances",
        use_pure = True
    )

    return connection