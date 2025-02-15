from working import convert

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"

def test_2():
    assert convert("10:30 PM to 8 AM")=="22:30 to 08:00"

def test_3():
    assert convert("9:60 AM to 5:60")=="ValueError"

if __name__=="__main__":
    main()