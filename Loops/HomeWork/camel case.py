import re
strin = input("Enter Camel Case: ")
output = []
for cha in strin:
    if cha.isupper():
        output.append("_")
        output.append(cha.lower())
    else: 
        output.append(cha)
print("snake_case: ", "".join(output))