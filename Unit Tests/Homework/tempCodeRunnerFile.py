def main():
    plate=input("Plate: ")
    if is_valid(plate):
            print("Valid")
    else:
            print("Invalid")

def is_valid(s):
    if 2<=len(s)<=6 :
        if s[:2].isalpha():


         if len(s)>4 and not s[2:3].isdigit():

                                    return True
        else:
             return False


if __name__=="__main__":
    main()





