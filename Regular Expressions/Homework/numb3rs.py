import re
import sys


def main():
   
    print(validate(input("IPv4 Address: ")))


def validate(ip):
     if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        li=ip.split(".")
        for l in li:
            if 0>int(l) or int(l) >255:
                return False
        return True
        
     else :
        return False
        
      


if __name__=="__main__":
    main()