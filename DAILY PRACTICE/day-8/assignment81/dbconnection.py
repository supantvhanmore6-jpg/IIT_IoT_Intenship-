import mysql.connector


def getconnection():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "smart_home_monitering_mqtt",
        use_pure = True
    )

    return connection