from itertools import product

def cartesian_product():
    first_a = list(map(int, input("Enter A (x, y) (space separated): ").split()))
    second_b = list(map(int, input("Enter B (x, y) (space separated): ").split()))
    
    result = product(first_a, second_b)
    
    print(*result)

def main():
    cartesian_product()
    
if __name__ == '__main__':
    main()