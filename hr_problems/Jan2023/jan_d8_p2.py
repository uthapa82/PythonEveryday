def main():
    number_of_country = int(input("Enter Number of Country Stamps: "))
    country_stamps = set()
    for i in range(number_of_country):
        country = input()
        country_stamps.add(country)
    
    print(len(country_stamps))
    
if __name__ == '__main__':
    main()