from numb3rs import validate
def main():
    test_1()
    test_2()

def test_1 ():
    assert validate(r"300.120.1.1")==False
    assert validate(r"200.120.1.1")==True
def test_2 ():
    assert validate(r"123.123.1")==False
    assert validate(r"123.1")==False

if __name__=="__main__":
    main()