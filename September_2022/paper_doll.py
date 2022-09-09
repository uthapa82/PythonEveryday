
def has_33(nums):
    for i in range(0, len(nums) - 1):
        # if nums[i:i+2] == [3,3]
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    
    return False 

# given a string return a string where for every character in 
# the original there are three characters 
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result 

# given three integers between 1 and 11, if their sum is less than or 
# equal to 21 return their sum less than or equal to 21
# blackjack(5, 6, 7) ---> 18
# blackjack(9, 9, 9) ---> 'BUST'
# blackjack(9, 9, 11) ---> 19
def blackjack(a, b, c):
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'
    
def main():
    list_1 = [1, 3, 3]
    print(has_33(list_1))
    print(paper_doll("Hello"))
    print(blackjack(5, 6, 7))
    print(blackjack(9, 9, 9))
    print(blackjack(9, 9, 11))

if __name__ == "__main__":
    main()