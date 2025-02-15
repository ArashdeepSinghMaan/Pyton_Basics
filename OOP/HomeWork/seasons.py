from datetime import datetime,date
import sys
import inflect

p = inflect.engine()

def main():
    DoB = input("Date of Birth (YYYY-MM-DD): ")
    result = days(DoB)
    if result:
        print(result)

def days(DoB):
    today = date.today()
    
    try:
        
        enDoB = datetime.strptime(DoB, '%Y-%m-%d')
    except ValueError:
        sys.exit("Invalid date")

    
    difference = today - enDoB
    minutes = difference*24* 60
    
    
    minutes_in_words = p.number_to_words(int(minutes), andword="")
    
    return f"{minutes_in_words.capitalize()} minutes"

if __name__ == "__main__":
    main()
