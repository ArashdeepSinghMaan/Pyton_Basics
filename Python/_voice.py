#str=input("Enter")
#my=str.swapcase()
#print(my)
#str=input()
#print(str.replace("a","b"))
""""
def main():
    str=input()
    print(convert(str))

def convert(img):
  img= img.replace(":)","🙂")
  # Change the order of the characters here
  img=img.replace(":(","🙁")
  return img

main()
"""
""""
str=int(input())
E=int(str*300000*300000)
print(E)
"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d)


def percent_to_float(p):
    return float(p)/100


main()