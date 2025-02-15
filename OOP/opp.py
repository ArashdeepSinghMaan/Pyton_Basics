
class Student:
    def __init__(self,name,house):

        
        self.name=name
        self.house=house
       
    def __str__(self):
        return f"{self.name} from {self.house}"
   

#Getter
    @property
    def house(self):
        return self._house
#Setter
    @house.setter
    def house(self,house):
        if house not in ["grf","ranc","Slytherin"]:
            raise ValueError("Invalid")    
        self._house=house


def main():
    student=get_name()
    
    print(student)     
    
    #print(f"{student.name} from {student.house}")


def get_name():
    
    name=input("Name:")
    house=input("House:")
    

    
    return Student(name,house)
   

if __name__=="__main__":
    main()

   
