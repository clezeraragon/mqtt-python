import paho.mqtt.publish as publish

message = {"time": 1561214540, "reactive": 222, "active": 222}
topic = "teste"
hostname = "3.83.224.205"
port = 1883
username = "admindoc"
password = "d0c88mQ073429"
keepalive = 60
print(hostname)
publish.single(topic,
               message,
               hostname=hostname,
               port=port,
               keepalive=keepalive,
               will=None,
               auth={'username': username, 'password': password})

