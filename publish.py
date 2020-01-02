import paho.mqtt.publish as publish


class Publish:

    def __init__(self, topic, msg, hostname, port, username, password):
        self._topic = 'topic'
        self._msg = 'msg'
        self._hostname = 'hostname'
        self._port = 'port'
        self._username = 'username'
        self._password = 'password'
        self.client_id = ""
        self.keepalive = 60
        self.publish = publish

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self,hostname):
        self._hostname = hostname

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self,topic):
        self._topic = topic

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self,port):
        self._port = port

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        self._password = password

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self,msg):
        self._msg = msg

    def send_publish(self):
        publish.single(self._topic,
                       self.msg,
                       hostname=self._hostname,
                       port=self._port,
                       client_id=self.client_id,
                       keepalive=self.keepalive,
                       will=None,
                       auth={'username': self._username, 'password': self._password})
