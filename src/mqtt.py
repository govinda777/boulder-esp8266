from umqtt.robust import MQTTClient

class Mqtt:

    def __init__(self):
        #This works for either ESP8266 ESP32 if you rename certs before moving into /flash 
        self.CERT_FILE = "/teste.cert.der"
        self.KEY_FILE = "/teste.private.der"

        #if you change the ClientId make sure update AWS policy
        self.MQTT_CLIENT_ID = "basicPubSub"
        self.MQTT_PORT = 8883

        #if you change the topic make sure update AWS policy
        self.MQTT_TOPIC = "sdk/test/Python"

        #Change the following three settings to match your environment
        self.MQTT_HOST = "a12sdqmvxrmcs4-ats.iot.us-east-1.amazonaws.com"

        self.mqtt_client = MQTTClient
        

    def check_msg(self):
        self.mqtt_client.check_msg()

    def wait_msg(self):
        self.mqtt_client.wait_msg()

    def on_message(self, topic, msg):
        print('Message topic: {}, payload: {}'.format(topic, str(msg)))

    def sub(self):
        try:    
            self.mqtt_client.subscribe(self.MQTT_TOPIC, qos = 1)
            
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

    def pub_msg(self, msg):
        try:    
            self.mqtt_client.publish(self.MQTT_TOPIC, msg)
            print("Sent: " + msg)
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

    def connect_mqtt(self):    
        try:
            with open(self.KEY_FILE, "r") as f: 
                key = f.read()

            print("Got Key")
                
            with open(self.CERT_FILE, "r") as f: 
                cert = f.read()

            print("Got Cert")	

            self.mqtt_client = MQTTClient(client_id=self.MQTT_CLIENT_ID, server=self.MQTT_HOST, port=self.MQTT_PORT, keepalive=5000, ssl=True, ssl_params={"cert":cert, "key":key, "server_side":False})
            self.mqtt_client.set_callback(self.on_message) 
            self.mqtt_client.connect()
            print('MQTT Connected')

        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise