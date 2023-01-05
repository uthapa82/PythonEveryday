import re
def main():
    number_of_test = int(input("Enter number of test cases: "))
    for i in range(number_of_test):
        user_string = input("Enter regex: ")
        
        try:
            re.compile(user_string)
            print(True)
            
        except re.error:
            print(False)
            
if __name__ == '__main__':
    main()