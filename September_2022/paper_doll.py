
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


# summer of 69: return the sum of the numbers in the array, except ignore
# sections of numbers starting with a 6 and extending to the next 9 
# summer_69([1, 3, 5]) ---> 9
# summer_69([4, 5, 6, 7, 8, 9]) ----->9
def summer_69(arr):
    total = 0
    add = True
    
    for num in arr:
        while add:
            if num!= 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
def main():
    list_1 = [1, 3, 3]
    print(has_33(list_1))
    print(paper_doll("Hello"))
    print(blackjack(5, 6, 7))
    print(blackjack(9, 9, 9))
    print(blackjack(9, 9, 11))
    print("Summer of 69")
    print(summer_69([1, 3, 5]))
    print(summer_69([4, 5, 6, 7, 8, 9]))

if __name__ == "__main__":
    main()