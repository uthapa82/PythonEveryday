# Python program to illustrate 
# math module 
import math

# iterating loops
def Main():
    print("Started: ")
    
    #calling the getInteger function and 
    # storing its returned value in the output variable 
    output = getInteger()
    for step in range(output):
        print("{} hello .".format(step))
    calculation()
# python program to illustrate
# function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result



# modules 
# standard library 
# math module 
def calculation():
    num = -85
    
    #fabs is used to get the absolute
    # value of a decimal 
    num = math.fabs(num)
    
    print(num)
    
# now we are required to tell python
# for 'Main' function existence 
if __name__ =="__main__":
    Main()