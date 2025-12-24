# install library/module for mqtt
#   pip install paho-mqtt

# import mqtt module
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid, reason_code, properties):
    print("message is published")

# creat a client to publish data
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_publish into our publisher
publisher.on_publish = on_publish

# send connect message to publisher
publisher.connect("localhost",1883)


# publish the message
while True:
    print("\n1. Light ON")
    print("2. Light OFF")
    print("3. Fan ON")
    print("4. Fan OFF")

    choice = input("Enter choice: ")

    if choice == "1":
        publisher.publish("home/light", "ON")
    elif choice == "2":
        publisher.publish("home/light", "OFF")
    elif choice == "3":
        publisher.publish("home/fan", "ON")
    elif choice == "4":
        publisher.publish("home/fan", "OFF")


# disconnect from broker
publisher.disconnect()
