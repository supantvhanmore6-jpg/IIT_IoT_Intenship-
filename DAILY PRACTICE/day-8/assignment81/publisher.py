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
publisher.publish("sensor/ldr/temp")
publisher.publish("sensor/ldr/intensity")
publisher.publish("sensor/lm35/temp")
publisher.publish("sensor/lm35/intensity")


# disconnect from broker
publisher.disconnect()
