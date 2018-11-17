from django.shortcuts import render
from django.http import HttpResponse
from localization import models

#####################################
import paho.mqtt.client as mqtt
import time
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from localization.models import Localization   
# Create your models here.


broker_host = "m20.cloudmqtt.com"
broker_port = "19641" 
broker_user_name = "gvzgfqqm"
password_to_server = "eB2dAtAmGpPS"

    

def sample_view(request):
    current_user = request.user
    print("Current_user_now: ",current_user)
    return current_user


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

    m_decode = str(msg.payload.decode("utf-8","ignore"))
    username = str(client._client_id.decode("utf-8","ignore"))

    user = User.objects.get(username=username)
    print("majster dzidoniuwa",user)
    temporary_localization = Localization(client = user ,posX = 20, posY = 10)
    temporary_localization.save()


    
    #encode_username(username)
    print("Message received: ",m_decode)
    #add_new_localization(username,m_decode)
   
    client.loop_stop()




####################################

def start(request):
    return render(request,'start.html')

def mainpage(request):
    return render(request, 'mainpage.html')
    
def view_user_id(request):

    client_username = request.user.username
    client = mqtt.Client(client_username)
    client.on_connect = on_connect
    client.on_log = on_log
    client.on_disconnect = on_disconnected
    client.username_pw_set(broker_user_name,password_to_server)
    client.connect(broker_host,int(broker_port))
    client.on_message = on_message
    

    print("KUPSZTAL: ", client._client_id)
    hahahaha = client._client_id


    client.loop_start()
    client.subscribe("Kacper/Dzidon",0)
    client.publish("Krzychu/wiadomosc","TEST_PASSED")
    time.sleep(1)

    time.sleep(1)

    


    

    client.loop_forever()
    client.disconnect()

    print("Po wiadomosci")
    html = "<html><body>User: %s.</body></html>" % hahahaha
    return HttpResponse(html)





 

