def main():
 numer =get_number()

 prio(numer)
def get_number():
    while True:
     numer=int(input("What ve?"))
     if numer>0:
       return numer

def prio(x):
   for _ in range(x):
     print("MEOW")

main()