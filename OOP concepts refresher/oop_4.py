# Encapsulation 
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self._salary = 5000
        self._num_bugs_solve = 0
        
        
se = SoftwareEngineer("Max", 25)
print(se.age, se.name)