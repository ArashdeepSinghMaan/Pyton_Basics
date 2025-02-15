from unitone import square

def main():
    test_sqaure()

def test_sqaure():
    try:
        assert square(2)==4
    except AssertionError:
        print("2 squarted was not 4")
    try:
        assert square(3)==9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert(-2)==4
    except AssertionError:
        print("-2 sqaured was not  4")
    try:
        assert(-3)==9
    except AssertionError:
        print("-3 sqaured was not  9")
    try:
        assert square(0)==0
    except AssertionError:
        print("0 squared was not 0")
if __name__=="__main__":
    main()