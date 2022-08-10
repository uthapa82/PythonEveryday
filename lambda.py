# difference between normal def function and lambda function 

def cube(y):
    return y*y*y

lambda_cube = lambda y:y*y*y
# using regular function 
print(cube(5))

# using lambda 
print(lambda_cube(5))

# without using lambda, both of them return cube of the given number 
# but while using def we need to define a function with a name cube
# and needed to pass a value to it, after execution we also needed to
# return the result from where the function was called using return 

# Using lambda we don't need to include return statement. It always 
# contains an expression that is returned, don't have to assign it to 
# a variable at all.

# Example lambda function with list comprehension 
def main():
    tables = [lambda x = x:x*10 for x in range (1, 11)]
    for table in tables:
        print(table())
        
if __name__ == '__main__':
    main()