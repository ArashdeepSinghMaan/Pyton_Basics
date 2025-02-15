def main():
    x=get_in()
    print(f"x is {x}")

def get_in():
    while True:
        try:
            x=int(input("what is x?"))
            

        except ValueError:
            print("x is  ot a n integer")
        else:
            break
    return x


main()