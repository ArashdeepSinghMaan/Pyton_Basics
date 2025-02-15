from PIL import Image
from PIL import ImageFilter
def main():
    with Image.open("Capture.PNG") as img:
     print(img.size)
     print(img.format)
     img=img.rotate(90)
     img=img.filter(ImageFilter.FIND_EDGES)
     img.save("ot.png")


main()