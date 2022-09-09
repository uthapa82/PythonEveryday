
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
# equal to 21 return their sum
def blackjack(a, b, c):
    pass
    
def main():
    list_1 = [1, 3, 3]
    print(has_33(list_1))
    print(paper_doll("Hello"))

if __name__ == "__main__":
    main()