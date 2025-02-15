from twttr import shorten
def main():
    test_1()
    test_2()

def test_1():
        assert shorten("PROBLEM") == "PRBLM"
        assert shorten("problem") == "prblm"
        assert shorten("ProBlem") == "PrBlm"

def test_2():
      assert shorten("12389") == "12389"
if __name__=="__main__":
    main()