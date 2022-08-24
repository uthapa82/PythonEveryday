# Encapsulation 

from email.mime import base


class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self._salary = 5000
        self._num_bugs_solve = 0
    
    def code(self):
        self._num_bugs_solve += 1
    # getter 
    def get_salary(self):
        return self._salary
    
    # setter 
    def set_salary(self, base_value):
        # check the value 
        # enforce constraints 
        # if value < 1000:
        #     self._salary = 1000
        # if value > 20000:
        #     self._salary = 20000
        self._salary = self._calculate_salary(base_value) 
    
    def _calculate_salary(self, base_value):
        if self._num_bugs_solve < 10:
            return base_value
        if self._num_bugs_solve < 100:
            return base_value * 2
        return base_value * 3
se = SoftwareEngineer("Max", 25)
print(se.age, se.name)

for i in range(70):
    se.code()

print(se._num_bugs_solve)  
se.set_salary(6000)
print(se.get_salary())