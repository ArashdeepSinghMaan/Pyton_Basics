from seasons import days

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert days("January 1,1999") == "Invalid date"

def test_2():
    assert days("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert days("1999-12-31") =="One thousand, four hundred forty mintues"
def test_3():
    assert days("1970-01-01")=="Fifteen million, seven hundred seventy-eight thousand eighty minutes"

if __name__ =="__main__":
    main()