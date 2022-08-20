# position, name, age, level, salary 
se_1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se_2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]
de_1 = ["Designer", "Adam", 25, "Senior", 7000]

# PEP 8 by convention class name should be CapsWord 
class SoftwareEngineer:
    
    # class attribute
    alias = "Keyboard Magician"
    
    def __init__(self, name, age, level, salary):
        # instance attrributes 
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    #instance method  
    def code(self):
        print(f"{self.name} is learning OOP")
        
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")
        
    def info(self):
        info = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return info
    
    # dunder method
    def __str__(self):
        info = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return info
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    # using decorators 
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000  

# instance 
se_1 = SoftwareEngineer("Max", 20, "Junior", 5000)

se_2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
se_3 = SoftwareEngineer("Lisa", 25, "Senior", 7000)

se_1.code()
se_2.code()

se_1.code_in_language("GO")
se_2.code_in_language("Python")

print(se_1.info())
print(se_2.info())

# using __str__ instead of info() 
print("\nPrinting information using only dunder method ")
print(se_1)
print(se_2)

# comparing if se_2 and se_3 are same
# if we have not used dunder method the following will compare memory location
# not the values 
print(se_2 == se_3)

print(se_1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))