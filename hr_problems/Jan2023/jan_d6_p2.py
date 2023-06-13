from collections import OrderedDict

def main():
    total_items = int(input("Enter total items: "))
    price_dict = OrderedDict()
    
    for i in range(total_items):
        name, price = input().rsplit(' ', 1) 
        price_dict[name] = price_dict.get(name, 0) + int(price)
    
    for k, v in price_dict.items():
        print(k, v)
        
if __name__ == '__main__':
    main()