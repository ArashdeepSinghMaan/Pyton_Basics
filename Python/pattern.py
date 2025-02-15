

def main():
    size = int(input("Enter size: "))
    square(size)

def square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()
