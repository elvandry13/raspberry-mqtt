# Libraries
import paho.mqtt.client as mqtt
import time

# MQTT Variables
broker = "broker.hivemq.com"
port = 1883
timeout = 60
topic = "test/elvandry"

# Callback function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic,qos=2)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, timeout)
client.loop_forever()
