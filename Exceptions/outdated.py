xx=input("Date:")
[x1,x2,x3]=xx.split("/")
print(x1,x2,x3)
print(x3+"-"+x1+"-"+x2)
if 1<=x2<=31 or 1<=x1<=12:
    raise ValueError
list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# compare x1 with list elements
#exceptions would be raised if day or month conditition is not satisfied.ion