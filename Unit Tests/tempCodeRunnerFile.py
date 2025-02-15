from unitone import square

def main():
    test_sqaure()

def test_sqaure():
    if square(2)!=4:
        print("Error!")
    if square(3)!=9:
        print("Error!")

if __name__=="__main__":
    main()