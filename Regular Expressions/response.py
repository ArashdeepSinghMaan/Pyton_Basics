from validator_collection import validators
def main():
    mail= input("What is your email address?")
    try:
        valid=validators.email(mail)
        print("Valid")
    except:
     print("Invalid")

if __name__=="__main__":
    main()