def main():
    plate=input("Plate: ")
    if is_valid(plate):
            print("Valid")
    else:
            print("Invalid")

def is_valid(s):
      if 2<=len(s)<=6 :
             if s[:2].isalpha():
                    if s[2:].isdigit() and s[2] !='0':
                           if s.isalnum():
                                return True
      else:
             return False
      
             

main()





