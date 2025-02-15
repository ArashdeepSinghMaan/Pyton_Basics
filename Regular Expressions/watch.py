import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if usem:= re.search(r"^https://|http://+ www ?\.?+youtube\.com/embed/xvFZjo5PgG0"):
        return True
    else:
        return False
    
 

if __name__=="__main__":
    main()
