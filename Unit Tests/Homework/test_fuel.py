from fuel import gauge, convert

def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

def test_1():
    assert gauge(convert("4/5")) == "80%"

def test_2():
    assert gauge(convert("5/5")) == "F"
    assert gauge(convert("99/100")) == "F"

def test_3():
    assert gauge(convert("1/500")) == "E"

def test_4():
    try:
        convert("1/0")
    except ZeroDivisionError:
        assert True
    else:
        assert False

def test_5():
    try:
        convert("5/4")
    except ValueError:
        assert True
    else:
        assert False

if __name__ == "__main__":
    main()
