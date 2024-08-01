import time
import json
import cv2


t = open('example_emotion_detail.json')
data = json.load(t)
BROKER_ADDR = 'pi5ub.local'
global conversion
emotions = {"mad","disgust", "fear","happy","sad","surprise"}
conversion = {
    "neutral":'Neutral',
    "mad": 'Mad',
    "disgust":'Disgusted',
    "fear": 'Fear',
    "happy":'Happy',
    "sad":'Sad',
    "surprise":'Surprised'
}
global dominantEmo 
dominantEmo = conversion['neutral']
global subEmo 
subEmo = conversion['neutral']
global folderPath 
folderPath = '/Users/robertmakowsky/Downloads/AI Art Library/'

def sub_cb(topic, msg):
    global subEmo 
    global dominantEmo 
    print((topic, msg))
    if topic == b'art/emotion':
        dominantEmo = msg.decode('utf-8')

def main(Emo1,Emo2):
    #fix the path otherwise it won't work
    image = cv2.imread(folderPath +Emo1+'-'+Emo2 +'.png')
    #image = cv2.imread('/Users/robertmakowsky/Downloads/AI Art Library/Happy-Fear.png')
    print(image)
    k = cv2.waitKey(1)
    cv2.imshow(Emo1 + Emo2,image) 
    time.sleep(10)
    cv2.destroyAllWindows()


def assign():
    global dominantEmo
    global subEmo
    dominantEmo = data.emotion_details[0]
    if data.emotion_details[0] >= 99:
        subEmo = dominantEmo
    else:
        subEmo = data.emotion_details[1]
while(True):
    #assign()
    main(dominantEmo,subEmo)
