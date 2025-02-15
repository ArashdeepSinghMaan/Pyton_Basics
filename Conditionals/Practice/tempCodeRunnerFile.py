name= input("What is your name ? ")
"""
if name =="Harry":
    print("Gryffindor")
elif name =="Hermione":
    print("slytherin")
"""

match name:
    case"Harry" |"Ron":
        print("Gryffindor")
    case"Hermione":
        print("slytherin")
    case _:
        print("who?")