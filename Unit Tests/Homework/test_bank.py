from bank import value
def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert value("Hello")==0
    assert value("hello")==0
def test_2():
    assert value("hen") ==20
    assert value("Hen")==20
def test_3():
    assert value("Lion") ==100
def test_4():
    assert value("100") == 100
    
if __name__=="__main__":
    main()