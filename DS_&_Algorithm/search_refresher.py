'''
Square root an integer using  Binary Search 
-Find largest integer i whose square is less than or equal to the given number 
-The values i*i is monotonically increasing, so the problem can be solved using binary search 
'''
def floor_sqrt(x):
    #base case 
    if x == 0 or x == 1:
        return x 
    
    start = 1
    end = x//2
    while start <= end:
        mid = (start + end )//2

        #check if x is a perfect square 
        if mid*mid == x:
            return mid 
        
        if mid*mid < x:
            start = mid + 1
            ans = mid 
        else:
            end = mid - 1
    return ans 

if __name__ == "__main__":
    x = int(input("Enter an integer: "))
    print("Square root or floor square root : ", floor_sqrt(x)) 