print("Expression:",end="")
xx=input()
x,y,z=xx.split(" ")
x=int(x)
z=int(z)
if y=="+":
    out=float(x+z)
    print(out)
elif y =="-":
    out=float(x-z)
    print(out)
elif y=="*":
    out=float(x*z)
    print(out)
elif y=="/":
    if z==0:
        print("not Posiible")
    else:
        out=float(x/z)
        print(out)
else:
    print("nahi ho sakda")




