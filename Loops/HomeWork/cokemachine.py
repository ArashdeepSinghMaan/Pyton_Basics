pending = int(50)
req = int(50)

def main():
    global pending, req
    while pending > 0:
        print("Insert Coin :")
        xx = int(input())
        pending -= xx
        if pending > 0:
            print("Pending Amount :", pending)
        else:
            print("Pending Amount : 0")
            break
    return xx

xx = main()
change = xx - req if pending <= 0 else 0
print("Change owed :", -pending)
