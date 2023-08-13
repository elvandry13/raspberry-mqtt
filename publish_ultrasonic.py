# Libraries
import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

# MQTT Variables
broker = "broker.hivemq.com"
port = 1883
timeout = 60
topic = "test/elvandry"

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

# Callback function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published")

# Main Program
def main():
     # Messages
     messages = ("%.2f" % distance())
     print(messages)

     # Publish messages
     client.publish(topic, payload=messages, qos=0, retain=False)

     # Sleep 2s
     time.sleep(2)


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

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
         GPIO.cleanup()
