cube = lambda x: x**3

def fibonacci(n):
    first_num = 0
    second_num = 1
    next_number = 0
    fib_list = []
    
    for i in range(n):
        fib_list.append(next_number)
        first_num = second_num
        second_num = next_number
        next_number = first_num + second_num
    
    return fib_list
  
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))