def main():
    word=input("Enter String:")
    print(shorten(word))

def shorten(word):
    cop=""
    kio="AEIOUaeiou"
    for c in word:
        if c not  in kio:
            cop = cop+c  
    return cop

if __name__=="__main__":
    main(  )