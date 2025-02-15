import re

email=input("What is your email?").strip()

if re.search(r"^[a-zA-Z_.].+@+[a-zA-Z_.]\.edu$",email):
    print("valid")
else:
    print("Invalid")