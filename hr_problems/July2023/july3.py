import re 

#fails test case 1
def initial_idea():
    test_cases = int(input())
    for i in range(test_cases):
        user_n = input()
        try :
            float(user_n)
            print("True")
        except:
            print("False")

def main():
    test_cases = int(input())
    for i in range(test_cases):
        user_n = input()
        if re.search(r'^[+-]?[0-9]*\.[0-9]+$', user_n):
            print("True")
        else:
            print("False")

if __name__ == '__main__':
    main()