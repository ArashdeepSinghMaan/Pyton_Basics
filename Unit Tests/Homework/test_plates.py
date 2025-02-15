from plates import is_valid
def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert is_valid("CS50") == True

def test_2():
    assert is_valid("Arashdeep")==False
def test_3():
    assert is_valid("PI3.OP")==False

if __name__=="__main__":
    main()