with open("names.txt","r") as file:
    #lines=file.readlines()

    for line in file:
   # print(f"hello,",line,end="")
        print("hello,",line.rstrip())