from PIL import Image 
import time
import signal
import subprocess
import os

def main(Emo1,Emo2):
    dominantEmo = Emo1
    subEmo = Emo2
    if os.path.exists('/Users/robertmakowsky/Downloads/' +Emo1+Emo2 +'.png'):
        print("the one piece is real")    
    p = subprocess.Popen(["open",'/Users/robertmakowsky/Downloads/' +Emo1+Emo2 +'.png'])
    time.sleep(10)
    return 1
while(True):
    main('fi','re')
    main('a','s')