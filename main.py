import os
from PIL import Image 

def main(Emo1,Emo2):
    dominantEmo = Emo1
    subEmo = Emo2
    im = Image.open("/Users/robertmakowsky/Downloads/" +dominantEmo+subEmo +".png")
    im.show()
    os.remove()
    return 1

while(True):
    main("fi","re")
    main("a","s")