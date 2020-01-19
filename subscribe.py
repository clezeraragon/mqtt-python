import paho.mqtt.client as mqtt
import requests
import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("teste")

def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))
    # print(json.loads(str(msg.payload)))
    payload = json.loads(msg.payload)
    print(payload)
    r = requests.post('http://127.0.0.1:8000/api/mqtt', json=payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("admindoc", password="d0c88mQ073429")

client.connect("3.83.224.205", 1883, 60)

client.loop_forever()