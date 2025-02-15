def main():
    xx=input()
    xy=convert(xx)
    print(xy)
   
def convert(xx):
    xy=xx.replace(":)","🙂")
    xy2=xy.replace(":(","🙁")
    return xy2
main()