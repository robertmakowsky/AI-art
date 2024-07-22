from PIL import Image 
from umqtt.simple import MQTTClient
import time
import subprocess
import os

CLIENT_NAME = 'mp1' #must be set to the name of the esp32 being used
BROKER_ADDR = 'pi5ub.local'
emotions = ['neutral', 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise'] 
global dominantEmo 
dominantEmo = emotions[0]
global subEmo 
subEmo = emotions[0]

def main(Emo1,Emo2):
    dominantEmo = Emo1
    subEmo = Emo2
    #fix the path otherwise it won't work
    if os.path.exists('/Users/robertmakowsky/Downloads/' +Emo1+Emo2 +'.png'):
        print("the one piece is real")

    p = subprocess.Popen(["open",'/Users/robertmakowsky/Downloads/' +Emo1+Emo2 +'.png'])
    time.sleep(10)
    return 1

while(True):
    t = MQTTClient(CLIENT_NAME, BROKER_ADDR)
    t.check_msg()
    if(): 
        dominantEmo =  MQTTClient(CLIENT_NAME, BROKER_ADDR)
        subEmo =  MQTTClient(CLIENT_NAME, BROKER_ADDR)
    main(dominantEmo,subEmo)