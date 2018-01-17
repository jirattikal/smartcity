import context
import paho.mqtt.client as mqtt
import random
import json
import time
mqttc = mqtt.Client()
mqttc.username_pw_set("eprchuzr","UEydS74yuz2b")
mqttc.connect("m14.cloudmqtt.com",11262, 60)

Gps=[] 
while True:
   
    for i in range(1,2):
        A=i
        B=str(A)
        topic="truck"+B
        print (topic)
        Gps1={}
        latitude=13.736717       ## Bangkok Thailand
        longitude=100.523186    
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
        R11=random.uniform(-0.001, 0.001)
        R12=random.uniform(-1, 1)
        R4R11=(R4*R11)/100000
        R4R12=(R4*R12)/100000
        
        latitude+=R4R11
        longitude+=R4R12
        Gps1["lat"]=latitude
        Gps1["lng"]=longitude
        #Gps1.append(latitude)
        #Gps1.append(longitude)
        Gps.append(Gps1)
        print("Gps=",Gps)
        G=str(Gps)
    
        X=json.dumps({"latitude":latitude,"longitude":longitude,"Engine RPM":R1,
                      "Coolant Temperature":R2,"Fuel System Status":R3,"Vehicle Speed":R4,
                      "Intake Manifold Pressure":R5,"Timing Advance":R6,"Intake Air Temperature":R7,
                      "Air Flow Rate":R8,"Absolute Throttle Position ":R9,"Fuel Pressure":R10,"GPS":G})      
        print(X)
        infot = mqttc.publish(topic, X, qos=0)
    time.sleep(3)
