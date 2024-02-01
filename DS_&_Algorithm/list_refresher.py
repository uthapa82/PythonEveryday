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
        
def remove_duplicate(lst):
    n = len(lst)
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
