students=[
       {"name":"Parag","State":"Madhya Pradesh","City":"Sagar"},
       {"name":"Swapnil","State":"Andaman","City":"Port Blair"},
       {"name":"Mayank","State":"Madhya Pradesh","City":None}
       
] 
for student in students:
    print(student["name"],student["State"],sep="  **;  ")
    