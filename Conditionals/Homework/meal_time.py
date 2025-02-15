def main():
    print("Time :",end="")
    xx=input()
    yy=convert(xx)
    if 7<=yy<=8 :
            print("breakfast time")
    elif 12<=yy<=13:
            print("lunch time")
    elif 18<=yy<=19:
            print("dinner time")
    
     


def convert(time):
        x,y=time.split(":")
        x=int(x)
        y=int(y)/60

        return x+y


if __name__=="__main__":
                main()