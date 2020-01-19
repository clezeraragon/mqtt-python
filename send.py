import paho.mqtt.publish as publish
from publish import Publish

message = '{"time": 95456542154512151212, "reactive": 222, "active": 222}'
topic = "teste"
hostname = "3.83.224.205"
port = 1883
username = "admindoc"
password = "d0c88mQ073429"
keepalive = 60
print(hostname)

send = Publish(topic, message, hostname, port, username, password)

send.send_publish()

