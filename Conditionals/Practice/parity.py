def main():
    x=int(input("what is x? "))
    if eve(x):
        print("x is even")
    else:
        print("odd")
def eve(x):
    #return True  if x%2==0  else False
     return x% 2==0
       

main()