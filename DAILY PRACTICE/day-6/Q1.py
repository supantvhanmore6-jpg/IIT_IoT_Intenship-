# import mysql connector
import datetime
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

id = int(input("Enter id : "))
tempraTURE = float(input("Enter temperature : "))
humidity =float(input("Enter humidity : "))
now = datetime.datetime.now()
formatted_time=now.strftime("%y-%m-%d %H:%M:%S")
timestamp=formatted_time

query = f"insert into sensor_readings values({id}, '{tempraTURE}', '{humidity}', '{timestamp}');"




# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()
