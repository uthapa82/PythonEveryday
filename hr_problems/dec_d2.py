from itertools import product
from collections import Counter

def cartesian_product():
    first_a = list(map(int, input("Enter A (x, y) (space separated): ").split()))
    second_b = list(map(int, input("Enter B (x, y) (space separated): ").split()))
    
    result = product(first_a, second_b)
    
    print(*result)

def calculate_revenue():
    no_of_shoes = int(input("Enter the total number of Shoes: "))
    shoe_size = Counter(input("Enter sizes available (space separated): ").split())
    number_of_customers = int(input("Enter total number of customers: "))
    
    total_amount = 0 
    for shoe in range(number_of_customers):
        size, amount = input("Enter Size and Cost of Shoe: ").split()
        if size in shoe_size.elements():
            total_amount += int(amount)
            shoe_size.update({size: -1})
    print("Total Revenue : $", total_amount)
    
def main():
    cartesian_product()
    calculate_revenue()
    
if __name__ == '__main__':
    main()