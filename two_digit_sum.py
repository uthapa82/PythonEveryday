# you are given two digit number N. Find the sum of its digits
# eg. N = 25 output: 7

def digitSum(N):
    number = str(N)
    firstDigit = number[0]
    secondDigit = number[1]
    result = int(firstDigit) + int(secondDigit)
    return result

def main():
    N = int(input("Two digit Number: "))
    print(digitSum(N))
    
if __name__ == "__main__":
    main()
