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
    # overriding 
    def work(self):
        print(f"{self.name} is coding..")
          
    def debug(self):
        print(f"{self.name} is debugging....")


class Designer(Employee):
    # overriding 
    def work(self):
        print(f"{self.name} is designing..")
    def draw(self):
        print(f"{self.name} is drawing.....")

se = SoftwareEngineer("Abhishek", 21, 6000, "Junior")
# print(se.name, se.age)
se.work()
se.debug()

de = Designer("Roshan", 26, 8000)
# print(de.name, de.age)
de.work()
de.draw()

# polymorphism 
emplyees = [SoftwareEngineer("Abhishek", 21, 6000, "Junior"),
            SoftwareEngineer("Roshan", 25, 10000, "Senior"),
            Designer("Ojha", 26, 8000)]

print("\n Polymorphism example.....")
def motivate_employees(employees):
    for employee in employees:
        employee.work()
        
motivate_employees(emplyees)