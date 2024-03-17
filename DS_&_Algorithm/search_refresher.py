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


# find the peak element in a list 
def peak_element(arr, n):
    start = 0
    end = n - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        
        #left neighbor greater
        if mid > 0 and arr[mid] < arr[mid - 1]:
            end = mid - 1 
        
        #right neighbor greater 
        elif mid < n - 1 and arr[mid] < arr[mid + 1]:
            start = mid + 1
        
        else:
            return mid 

def count_binary_1(arr,low,high):
    
    while low <= high :
        mid = low + ((high - low)//2)

        # check if the element at middle index is last 1
        if mid == high  or arr[mid+1] == 0 and arr[mid] == 1:
            return mid + 1
        
        # if element is not last 1, check right side 
        if arr[mid] == 1:
            return count_binary_1(arr, mid+1, high)
        
        return count_binary_1(arr, low, mid-1)
    
    return 0

# find the floor of largest element in list
# Find element K such that it's less than or equal to x
def floor_search(arr,low, high, x):

    while low <= high:
        if arr[high] <= x:
            return high
        mid = low + ((high - low)//2)
        if arr[mid] == x:
            return mid 
        
        # x lies between mid-1 and mid 
        if mid > 0 and arr[mid-1] <=x and x < arr[mid]:
            return mid-1
        
        # if x is smaller than mid 
        if x < arr[mid]:
            return floor_search(arr, low, mid-1, x)
        
        return floor_search(arr,mid+1, high,x)
    return -1
    
if __name__ == "__main__":
    # x = int(input("Enter an integer: "))
    # print("Square root or floor square root : ", floor_sqrt(x))
    arr = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    print(count_binary_1(arr, 0, len(arr)-1)) 