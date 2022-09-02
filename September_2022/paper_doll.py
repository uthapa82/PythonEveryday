
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    
    return False 

def main():
    list_1 = [1, 3, 3]
    print(has_33(list_1))

if __name__ == "__main__":
    main()