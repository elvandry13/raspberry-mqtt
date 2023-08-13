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
 
def on_publish(client,userdata,result):
	print("data published")

# Main Program
def main():
     # Messages
     messages = "Hello from Raspberry!"

     # Publish messages
     client.publish(topic, payload=messages, qos=0, retain=False)

     # Sleep 5s
     time.sleep(5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(broker, port, timeout)

if __name__ == '__main__':
    try:
        while (True):
             main()
    except KeyboardInterrupt:
         print("Stopped by user")
