name =input("What is your name?")

#file=open("names.txt","a")
with open("names.txt","a") as file:
    file.write(f"{name}\n")
#file.close()

