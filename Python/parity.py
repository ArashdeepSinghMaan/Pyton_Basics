def main():
        x=int(input("Enter number"))
        if checker(x):
            print("Even")
        else:
            print("ODD")

def checker(n):
       return n % 2==0  
       
            

main()