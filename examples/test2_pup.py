import context
import paho.mqtt.client as mqtt
import random
import json
import time
mqttc = mqtt.Client()
mqttc.username_pw_set("eprchuzr","UEydS74yuz2b")
mqttc.connect("m14.cloudmqtt.com",11262, 60)

Y="k"

def Data(self):
    random.randint(0,100)
topic=["truck"+str(i) for i in range(10)]
for i in range:
    print(topic[i])
    #print(To)

    R1=random.randint(0,8000)
    R2=random.randint(0,500)
    R3=random.randint(0,100)
    R4=random.randint(0,200)
    R5=random.randint(1,100)
    R6=random.randint(1,100)
    R7=random.randint(1,100)
    R8=random.randint(1,100)
    R9=random.randint(1,100)
    R10=random.randint(1,100)
    
    X=json.dumps({"Engine RPM":R1,"Coolant Temperature":R2,"Fuel System Status":R3,"Vehicle Speed":R4,"Intake Manifold Pressure":R5,
                  "Timing Advance":R6,"Intake Air Temperature":R7,"Air Flow Rate":R8,"Absolute Throttle Position ":R9,"Fuel Pressure":R10})      
    print(X)
    #infot = mqttc.publish(To, X, qos=0)
    #time.sleep(5)
