import paho.mqtt.publish as publish

publish.single("teste", "gdfgdfg", hostname="host", port=1883, client_id="", keepalive=60,
               will=None, auth= {'username':"1", 'password':"1"})
