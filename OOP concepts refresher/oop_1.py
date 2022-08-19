# position, name, age, level, salary 
se_1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se_2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]

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

# instance 
se_1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se_1.name, se_1.age)

print(SoftwareEngineer.alias)
se_2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(SoftwareEngineer.alias)