# nested list 
List = [["Geeks", "For"], ['Geeks']]
print("\n Multi-dimensional List: ")
print(List[-1])

# tuples cannot be modified they are immutable 
#creation of set 
Tuple1 = tuple(List)
print("Initial empty Tuple: ")
print(Tuple1)

# set is an unordered collection of data type that is iterable, mutable and has no duplicate elements 
set1 = set("GeeksForGeeks")
print(set1)
print("Geeks" in set1)

Dict = {1:"Geeks", 2:"For", 3:"Geeks"}
print(Dict)
print(Dict.get(1))

# Bitwise Operators in Python
print("**********Bitwise Operators in Python ")
a = 10
b = 4
# print bitwise AND operation
print(a & b)

# print bitwise OR operation
print(a | b)

# print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)

# read two numbers from input and typecasts them to int using
# list comprhension 
x,y = [int(x) for x in input().split()]

t = 21
print(hex(t))