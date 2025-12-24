from dbconnection import getconnection
from executequery import executeQuery
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print(f"message :{message.payload}")

    flag=1
    if(flag):
        query="INSERT IGNORE INTO status (id, light_status, fan_status) VALUES (1, 'OFF', 'OFF');"
        executeQuery(query=query)
        flag=0

    status=(message.payload.decode())
    if message.topic=="home/fan":
        query=f"updat status SET fan_status='{status}' WHERE id=1;"
        executeQuery(query=query)
        print("fan turned", status)

    if message.topic=="home/light":
        query=f"update status SET light_status='{status}' WHERE id=1;"
        executeQuery(query=query)
        print("Light turned", status)

 
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_message into our subscriber
subscriber.on_message = on_message

# send connect message to publisher
subscriber.connect("localhost",1883) 

# subscribe for topic
subscriber.subscribe("home/light")
subscriber.subscribe("home/fan")


# keep subscriber running continuously
subscriber.loop_forever()
