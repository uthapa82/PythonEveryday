def start_end_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

def print_name():
    print("Alex")
    
#print_name = start_end_decorator(print_name)

print_name()
result = add5(10)
print(result)