"""
Deep Thought
x=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if x=="42":
    print("Yes")
elif x=="forty-two" or x =="forty two" :
     print("Yes")
else:
   print("No")
   """""

"""""
Home Federal Savings Bank
x=input("Greeting:")
if x.startswith("Hello") or x.startswith("hello"):
    print("$0")
elif x.startswith("H") or x.startswith("h"):
    print("$20")
else:
    print("$100")
"""""
""""
#File Extension
xo=input("Enter file format")
if xo==".gif":
    print("Image/",xo)
elif xo==".jpeg":
    print("Image/",xo)
elif xo==".jpg":
    print("Image/",xo)
elif xo==".pdf":
    print("Document/",xo)
elif xo==".txt":
    print("Document/",xo)
else:
    print("Do not Know")
    
"""""
"""""
Math Interpreter
expression=input("Enter ")
x, y, z = expression.split(" ")


final=eval((x+y+z))
print(f"{final:.1f}")
"""""
"""""
#meal time
BREAKFAST_START = 7
BREAKFAST_END = 11
LUNCH_START = 12
LUNCH_END = 15
DINNER_START = 18
DINNER_END = 20
def main():
    x=input("What is time?")
    time=convert(x)
if BREAKFAST_START <= time <= BREAKFAST_END:
            # Print breakfast time
            print("Breakfast time")
elif LUNCH_START <= time <= LUNCH_END:
            # Print lunch time
            print("Lunch time")
elif DINNER_START <= time <= DINNER_END:
            # Print dinner time
            print("Dinner time")

"""""
"""""
# Define the constants for the meal time ranges
BREAKFAST_START = 7
BREAKFAST_END = 11
LUNCH_START = 12
LUNCH_END = 15
DINNER_START = 18
DINNER_END = 20

def main():
    # Ask the user to enter a time
    x = input("What is time? ")
    convert(x)


    # Use a try-except block to handle possible exceptions
 
        # Call the convert function and assign its return value to time
   
        # Check if the time falls within any of the meal time ranges
if BREAKFAST_START <= convert(x) <= BREAKFAST_END:
            # Print breakfast time
            print("Breakfast time")
elif LUNCH_START <= convert(x) <= LUNCH_END:
            # Print lunch time
            print("Lunch time")
elif DINNER_START <= convert(x) <= DINNER_END:
            # Print dinner time
            print("Dinner time")
        # If none of the conditions are met, do not print anything
   

def convert(time):
    # Split the input by colon and convert each part to a float
    z, y = time.split(":")
    y = float(y) / 60
    k = float(z) + y

    # Return the converted time as a float
    return k

if __name__ == "__main__":
    main()
"""""
BREAKFAST_START = 7
BREAKFAST_END = 11
LUNCH_START = 12
LUNCH_END = 15
DINNER_START = 18
DINNER_END = 20

def main():
    try:
        # Ask the user to enter a time
        x = input("What is the time? ")

        # Call the convert function and assign its return value to time
        time = convert(x)

        # Check if the time falls within any of the meal time ranges
        if BREAKFAST_START <= time <= BREAKFAST_END:
            # Print breakfast time
            print("Breakfast time")
        elif LUNCH_START <= time <= LUNCH_END:
            # Print lunch time
            print("Lunch time")
        elif DINNER_START <= time <= DINNER_END:
            # Print dinner time
            print("Dinner time")
        else:
            # If none of the conditions are met, do not print anything
            print("Not mealtime")
    except ValueError:
        print("Invalid input. Please enter time in HH:MM format.")

def convert(time):
    # Split the input by colon and convert each part to a float
    z, y = time.split(":")
    y = float(y) / 60
    k = float(z) + y

    # Return the converted time as a float
    return k

if __name__ == "__main__":
    main()
