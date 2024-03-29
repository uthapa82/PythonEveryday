import re

def extract_max(input):
    # get a list of all numbers separated by 
    # lower case characters
    # \d+ is a regular expression which means 
    # one or more digit 
    # output will be like ['100', '564', '365']
    numbers = re.findall('\d+', input)
    
    # now we need to convert each number into integer 
    # int(string) converts string into integer 
    # we will map int() function onto all elements
    # of number list
    numbers = map(int, numbers)
    print(max(numbers))

def main():
    user_input = input("Please enter any Alphanumeric value: ")
    extract_max(user_input)
    
if __name__ == "__main__":
    main()