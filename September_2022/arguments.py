# arg return back tuple 
# order matters (*args, **kwargs) 

def my_func(*args):
    # returns 5% of the sum of a and b
    for item in args:
        print(item)
    # return sum((args)) * 0.05

#keyword args returns dictionary 
def my_func2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit is {}'.format(kwargs['fruit']))
    else:
        print("I did not find any fruits")

def combo(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs['food']))
    
def main():
    print(my_func(40, 60, 20, 10))
    my_func2(fruit='apple', veggie='lettuce')
    combo(10, 20, 30, fruit='orange', food='eggs')
    
if __name__ == "__main__":
    main()