import paho.mqtt.client as mqtt
import time
# Create your models here.


broker_host = "m20.cloudmqtt.com"
broker_port = "19641" 
user_name = "gvzgfqqm"
password_to_server = "eB2dAtAmGpPS"


#------------------------------------------------------
# err codes:
#
# 0: Connection successful
# 1: Connection refused – incorrect protocol version
# 2: Connection refused – invalid client identifier
# 3: Connection refused – server unavailable
# 4: Connection refused – bad username or password
# 5: Connection refused – not authorised
# 6-255: Currently unused.
#------------------------------------------------------


def on_log(client, userdata, lever, buf):
    print("log: "+buf)


def on_connect(client, userdata, flags, err):
    if int(err) == 0:
        print("Connected OK. Err code = ", err)
    else:
        print("FAIL: Err code: ",err)


def on_disconnected(client, userdata, err):
    print("Disconnected. Err code = ",int(err))



def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("Message received: ",m_decode)


# ********************************************
# *                                          *
# *               Main code                  *
# *                                          *
# ********************************************


client = mqtt.Client("Krzychu")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnected
client.username_pw_set(user_name,password_to_server)
client.connect(broker_host,int(broker_port))

client.on_message = on_message
client.loop_start()
client.subscribe("Kacper/Dzidon",0)
client.publish("Krzychu/wiadomosc","Kacper to Dzidoń")
time.sleep(1)

time.sleep(1)


client.loop_forever()
client.disconnect()