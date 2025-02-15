def main():
    inxs=input("Greeting:")
    print("$",value(inxs))

def value(inxs):
    xx=inxs.strip().lower()
    if xx.startswith("hello")   :
         return 0

    elif xx[0]=="h":
        return 20
    else :
        return 100

if __name__=="__main__":
    main()