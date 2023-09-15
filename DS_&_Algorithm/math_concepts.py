from math_modules import trail_zero

def sum_of_numbers(n):
    result = n * (n+1) / 2

    return result

def count_digits(digit):
    count = 0
    temp_digit = digit 

    while temp_digit != 0 :
        temp_digit = temp_digit // 10

        count += 1
    
    return count 

def is_palindrome(num):
    rev = 0
    temp = num

    while temp != 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit
        temp = temp // 10
    
    return rev == num

# Time compleity theta(n)
# space complexity O(1) --> constant 
def fact_number(value):
    result = 1
    
    for i in range(2, value + 1):
        result = result * i
    
    return result

# recursive method 
# time complexity T(n) = T(n-1) + theta(1)
def fact_number_rec(value):
    #base case 
    if value == 0:
        return 1
    
    return value * fact_number_rec(value - 1)

def main():
    # n = int(input("Enter n : "))
    # print("Sum of n natural numbers: ", sum_of_numbers(n))

    # digit = int(input("\nEnter digit(s): "))
    # print("Total digits :", count_digits(digit))

    # num = int(input("\nEnter num: "))
    # print("Palindrome: ", is_palindrome(num))

    # value = int(input("\nEnter value: "))
    # print(f"Factorial of {value} is:", fact_number(value))
    # print(f'Factorial of {value} using recursive method is:', fact_number_rec(value))

    trail_check_num = int(input("\nEnter to find zeros in a factorial (n!) : "))
    print(trail_zero(trail_check_num))

    
if __name__ == '__main__':
    main()