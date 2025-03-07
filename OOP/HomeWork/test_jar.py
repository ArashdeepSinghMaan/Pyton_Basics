from jar import Jar


def test_init():
    jar=Jar()
    assert jar.capacity == 12
    jar2=Jar(3)
    assert jar.capacity == 3



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(6)
    assert jar.size ==6
    jar.deposity (2)
    assert jar.size ==8


def test_withdraw():
    jar =Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size ==4