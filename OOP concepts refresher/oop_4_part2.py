# Properties 
# more pythonic way of using getter and setter by using decorators   

class SoftwareEngineer:
    def __init__(self):
        self._salary = None
      
    
    def code(self):
        self._num_bugs_solve += 1
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value
        
    @salary.deleter
    def salary(self):
       del  self._salary 
    

se = SoftwareEngineer()

se.salary = 6000
print(se.salary)

# del se.salary
