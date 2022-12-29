# collections.Counter() is a container that stores elements as dictionary keys 
from collections import Counter

def main():
    no_of_shoes = int(input("Enter the number of shoes: "))
    shoes = input("Enter shoes sizes in the shop: ")
    shoe_sizes = Counter(shoes.split())
    number_of_customers = int(input("Enter numbers of Customers: "))
    total_amount  = 0
    
    for i in range(number_of_customers):
        size, amount = input().split()
        
        # check availability 
        if size in shoe_sizes.elements():
            total_amount += int(amount)
            shoe_sizes.update({size: -1})
    print(total_amount)
    

if __name__ == '__main__':
    main()
    
