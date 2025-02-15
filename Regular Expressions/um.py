import re
import sys

def main():
    print(count(input("Text:")))

def count(s):
    li=re.findall(r"\b\W*um\W",s)
    xo=int(len(li))
    return xo

if __name__=="__main__":
    main()                      