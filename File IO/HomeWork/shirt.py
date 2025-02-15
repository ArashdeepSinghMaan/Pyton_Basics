import sys
from os.path import splitext
from PIL import Image,ImageOps

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    foo_1=splitext(sys.argv[1])
    foo_2=splitext(sys.argv[2])
    if cheker_extension(foo_1) == False:
        sys.exit("Invalid input")
    if cheker_extension(foo_2) == False:
        sys.exit("Invalid input")
    if foo_1.lower()!=foo_2.lower():
        sys.exit("Input and output have different extensions")

    try:
        img_1=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    img_2=Image.open("shirt.png")
    size=img_2.size
    mpp=Image.Ops.fit(img_1,size)
    mpp.paste(img_2,img_2)
    mpp.save(sys.argv[2])

    
def cheker_extension(foo):
    if foo in [".jpg",".jpeg",".png"]:
        return True
    return False
    



if __name__=="__main__":
    main()