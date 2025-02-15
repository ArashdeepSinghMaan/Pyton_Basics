print("Input")
str=input()
kio="AEIOUaeiou"
for c in str:
    for d in kio:
     if c==d:
        c=""
    print(c,end="")