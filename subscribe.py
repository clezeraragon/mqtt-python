
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("teste")

def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("admin", password="1234")

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()