import time
from PIL import Image 

global im
im = Image.open("/Users/robertmakowsky/Downloads/default.JPG")
im.show()
def main(Emo1,Emo2):
    dominantEmo = Emo1
    subEmo = Emo2
    im.close()
    im = open("/Users/robertmakowsky/Downloads/" +dominantEmo+subEmo +".png")
    im.show()
    return 1

while(True):
    main("fi","re")
    main("a","s")