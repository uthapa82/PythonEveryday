# inherits, extends, override 
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary 

    def work(self):
        print(f"{self.name} is working..")
        
class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level


class Designer(Employee):
    pass 

se = SoftwareEngineer("Abhishek", 21, 6000, "Junior")
# print(se.name, se.age)
se.work()

de = SoftwareEngineer("Roshan", 26, 8000, "Senior")
# print(de.name, de.age)
de.work()