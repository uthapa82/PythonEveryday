'''
-creating/accessing/append() all takes O(1) constant time 
-Insertion using insert() method takes O(n) linear time 
-extend() add multiple elements at the same time at the end of the list 
-takes O(n), remove()= O(n), pop= O(1) for last element, O(n) for first 
 and middle elements 
list/dictionary/set/Generator comprehensions 
output_list = [output_exp for var in input_list if (var satisfies this condition)]
eg. [var for var in input_list if var % 2 == 0]

output_dict = {key:value for (key,value) in iterable if (key, value satisfy this condition)}
eg. {var:var **3 for var in input_list if var % 2 != 0}

output_set = {var for var in input_list if var % 2 == 0}
    - very similar to list only difference is set use curly brackets 

generator_output = (var  for var in input_list if var % 2 == 0)
for var in generator_output:
    print(var, end = ' ')

    - very similar to list comprehensions one difference is that generator use small brackets (wheras list - [])
    - also generator don't allocate memory for the whole list, instead they generate each value one by one , more 
    memory efficient 
'''

# array second largest element in a list 
# time complexity : O(n)
def max_second(arr, arr_size):
    if arr_size < 2:
        print("Invalid Input: ")
        return
    # can also use: float('-intf')
    first = second = -2147483648
    for i in range(arr_size):
        if (arr[i] > first):
            second = first 
            first = arr[i]

        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
        
    if (second == -2147483648):
        print("No second largest element")
    else: 
        print("Second largest element is ", second)

# check if the list is sorted - O(n)
def is_sorted(lst, arr_len):
    if (arr_len == 0 or arr_len == 1):
        return True
    
    for i in range(1, arr_len):
        if (lst[i-1] > lst[i]):
            return False
    
    return True

'''
    reversing list
    #swap alternative
    temp = lst[left]
    lst[left] = lst[right]
    lst[right] = temp
    left += 1
    right -= 1
'''
def rev_lst(lst):
    
    # approach 1
    new_l = lst[::-1]

    # two pointer approach O(n) time complexity 
    start = 0
    e = len(lst) - 1
    while start < e:
        lst[start], lst[e] = lst[e], lst[start]
        start = start + 1
        e = e - 1

# time complexity O(n), auxiliary space: O(n)    
def remove_duplicate(lst):
    n = len(lst)
    # return if array is empty or 
    # contains a single element 
    if n == 0 or n == 1:
        return n
    
    temp_lst = list(range(n))
    j = 0

    # compare every pair of list 
    for i in range(0, (n - 1)):
        if lst[i] != lst[i+1]:
            temp_lst[j] = lst[i]
            j += 1

    #last element in list 
    temp_lst[j] = lst[n-1]
    j += 1

    #change the original list 
    # for k in range(0, j):
    #     lst[k] = temp_lst[k]

    return temp_lst[:j]

# duplicate without extra space
# time complexity: O(n) auxiliary space: O(1)
# just maintain a separate index for same array 
def remove_duplicate_2(lst):
    n = len(lst)

    if n == 0 or n == 1:
        return n
    
    j = 0

    for i in range(0, n - 1):
        if lst[i] != lst[i+1]:
            lst[j] = lst[i]
            j += 1
    
    lst[j] = lst[n-1]
    j += 1

    return lst[:j]

# left rotate a list by one 
def left_rotate(lst):
    
    # using slicing 
    # return (lst[1:] + lst[0:1])

    # using append/pop
    # lst.append(lst.pop(0))
    # return lst

    # using iterative method 
    n = len(lst)
    x = lst[0]
    
    for i in range(1, n):
        lst[i - 1] = lst[i]
    
    lst[n - 1] = x

    return lst 

# one odd occuring 
# eg. arr = [1,2,3,2,3,1,3] => 3 (as 3 occurs an odd number of times)
# we can run two nested loops and compare but won't be efficient: O(n^2)
# bitwise XOR of all the elements: O(n), auxiliary space O(1)
def odd_occuring_number(lst):
    result = 0
    for element in lst:
        result = result ^ element
    
    return result

# Comprehensions in python 
def comprehension_example(lst):
    list_comprehen = [x for x in lst if x % 2 == 0]

    # set comrprehension 
    s1 = {x for x in lst if x % 2 == 0}

    # dictionary comprehension 
    d1 = {x:x**2 for x in lst}

    d2 = {x:f"ID{x}" for x in range(len(lst))}

    lst2 = ['a', 'b', 'c']
    d3 = {lst[i]:lst2[i] for i in range(len(lst2))}

    # better option for d3 
    d3_better = dict(zip(lst, lst2))

    # inverting a dictionary (key becomes value and value becomes key)
    d_inverted = {v:k for (k, v) in d3_better.items()}

    print(d_inverted)

# largest element in a list linear time 
def largest_in_lst(lst):
    if not lst:
        return None 
    else:
        result = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > result:
                result = lst[i]
        return result 
    
# second largest element in a list 
# naive solution - theta(n) two traversal of list 
def getMax(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        result = max(result, lst[i])
    return result

def second_largest_in_lst(lst):
    if len(lst) <= 1:
        return None 
    
    lar = getMax(lst)
    slar = None
    for x in lst:
        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(slar, x)
    return slar

# time complexity theta(n) but only one traversal
def second_largest_optimal(lst):
    if len(lst) <= 1:
        return None
    lar = lst[0]
    slar = None
    for x in lst[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar

# check if a list is sorted 
def check_sorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst)):
        if lst[i] <= lst[i+1]:
            return True
        else:
            return False

# reverse a list 
def reverse_list(lst):
    s = 0
    e = len(lst) - 1
    while s < e:
        lst[s], lst[e] = lst[e], lst[s]
        s = s + 1
        e = e - 1

# removes the element 
def remove_duplicate(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
        
    return unique_lst

#left rotate a list 
def left_rotate(lst):
    #using direct method 
    # lst.append(lst.pop(0))
    # lst[1:] + lst[0]
    n = len(lst)
    x = lst[0]
    for i in range(1, n):
        lst[i - 1] = lst[i]
   
    lst[n-1] = x
    return lst

def mean_median(arr, n):
    
    mean_arr = 0
    for item in arr:
        mean_arr += item
    
    print("Mean: ", mean_arr//n)

    arr.sort()
    #check if there are odd element 
    if n % 2 != 0:
        print("Median: ", arr[(n//2)])
    
    else: 
        print("Median: ", (arr[n//2] + arr[(n//2) -1])//2)
    
if __name__ == '__main__':
    mean_median([2,8,3,4], 4)
