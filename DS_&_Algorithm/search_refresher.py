'''
Square root an integer using  Binary Search 
-Find largest integer i whose square is less than or equal to the given number 
-The values i*i is monotonically increasing, so the problem can be solved using binary search 
'''
#time O(sqrt(n))
def floor_sqrt_naive(x):
    i = 1
    while i*i <= x:
        i += 1
    return i - 1
    
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

# First occurence Binary Search iterative method 
def first_Occurence(arr, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid 
            else:
                high = mid - 1
    
    return -1

# index of last occurence 
# naive solution O(n)
def last_occurence_naive(arr, x):
    for i in reversed(range(len(arr))):
        if arr[i] == x:
            return i
    
    return -1

# efficient solution O(logn)
def last_occurence(arr, n, x):
    low  = 0
    high = n - 1
    while low <= high:
        mid = (low + (high - low)//2)
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
                return mid 
            else:
                low = mid + 1
    return -1

# count occurence, efficient solution 
# O(logn) + O(logn) ==> O(logn)
def count_occur(arr, n, x):
    first = first_Occurence(arr,n, x)
    if first == -1:
        return 0
    else:
        return last_occurence(arr, n, x) - first + 1

  
if __name__ == "__main__":
    # x = int(input("Enter an integer: "))
    # print("Square root or floor square root : ", floor_sqrt(x))
    arr =[5, 10, 10, 10, 20, 20]
    x = 11
    print(count_occur(arr, len(arr),x)) 