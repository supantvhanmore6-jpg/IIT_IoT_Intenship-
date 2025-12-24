from dbconnection import getconnection
from executequery import executeQuery
import paho.mqtt.client as mqtt
import json
ldr_temp=lm35_temp=lm35_intensity=ldr_intensity=None

def on_message(client, userdata, message):
    print(f"message :{message.payload}")
    global ldr_temp,ldr_intensity,lm35_intensity,lm35_temp

    data=float(message.payload.decode())
    if message.topic=="sensor/ldr/temp":
        ldr_temp=data
        print("ldr_temp recevied.")

    elif message.topic=="sensor/ldr/intensity":
        ldr_intensity=data
        print("ldr_intensity recevied.")
              
    elif message.topic=="sensor/lm35/temp":
        lm35_temp=data
        print("lm35_temp recevied.")

    elif message.topic=="sensor/lm35/intensity":
        lm35_intensity=data
        print("lm35_intensity recevied.")

    if lm35_intensity is not None and lm35_temp is not None and ldr_temp is not None and ldr_intensity is not None :
        query=f"insert into device_readings values({ldr_temp},{ldr_intensity},{lm35_temp},{lm35_intensity});"
        executeQuery(query=query)
        print("data added succesfully")
        ldr_temp=lm35_temp=lm35_intensity=ldr_intensity=None
 
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_message into our subscriber
subscriber.on_message = on_message

# send connect message to publisher
subscriber.connect("localhost",1883) 

# subscribe for topic
subscriber.subscribe("sensor/ldr/temp")
subscriber.subscribe("sensor/ldr/intensity")
subscriber.subscribe("sensor/lm35/temp")
subscriber.subscribe("sensor/lm35/intensity")

# keep subscriber running continuously
subscriber.loop_forever()
