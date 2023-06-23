import random 
import time 
import sys 
from Adafruit_IO import MQTTClient

AIO_FEED_ID ="power-switchboard"
AIO_USERNAME ="SuSername"
AIO_KEY ="aio_lHJe78TRaMAFUB0kVvIZLjEmVsWg"
def connected(client):
    print("ket noi thanh cong ")
    client.subscribe(AIO_FEED_ID)
def subscribe(client, userdata,mid, granted_qos):
    print("Subscribe thanh cong ")
def disconnected(client):
    print("ngat ket noi")
    sys.exit(1)
def message(client, feed_id, payload):
    print("Nhan du lieu: "+payload)
client=MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect= connected
client.on_disconnect= disconnected 
client.on_message= message
client.on_subscribe= subscribe 
client.connect()
client.loop_background()

while True:
    value =random.randint(0,130)
    print("Cap nhap: ",value)
    client.publish("speed-on-highway",value)
    time.sleep(3)
