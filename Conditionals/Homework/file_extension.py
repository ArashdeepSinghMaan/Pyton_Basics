print("File Name:",end="")
xx=input()

if xx.endswith(".gif"):
    print("image/gif")
elif xx.endswith(".jpg"):
    print("image/jpg")
elif xx.endswith(".jpeg"):
    print("image/jpeg")
elif xx.endswith(".png"):
    print("image/png")
elif xx.endswith(".pdf"):
    print("application/pdf")
elif xx.endswith(".txt"):
    print("application/txt")
elif xx.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")