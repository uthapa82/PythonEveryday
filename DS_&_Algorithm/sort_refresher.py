'''
sorted(iterable, key, reverse=False)
Parameters:
    iterable : sequence(list, tuple, string) or collection(dictinary, set, frozensets)
'''
def sort_methods(arr):
    # does unicode comparison for string char by char
    # always returns a sorted list, doesn't effect the original sequence 
    # complexity O(nlog(n))

    sorted_result = sorted(arr)

    # sort() function is similar but makes changes to the original sequence
    # can only used in lists 
    # time complexity O(n log(n))
    sorted_result = arr.sort()
    
    # a sorting algorithm is said to be stable if two objects with equal keys 
    # appear in the same order in sorted output as they appear in input data set 
    # stable algorithm stable by nature: Bubble sort, insertion sort, merge sort
    # count sort 
    test_list = [("Adam", 50), ("John", 50), ("Tom", 80)]
    test_list.sort()

# bubble sort 
# time complexity O(n^2)
def bubble_sort(arr):
    n = len(arr) - 1

    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# slightly optimized bubble sort 
# stops when the list become sorted
def bubble_sort_optimized(arr):
    n = len(arr) - 1

    for i in range(n):
        swapped = False 
        for j in range(n-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if swapped == False:
            return

# selection sort, time complexity: O(n^2)
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

# insertion sort 
# two half sorted vs unsorted sub-array 
# similar to playing cards 
# best case :O(n), worst case: O(n^2)
def insertion_sort(arr):
    n = len(arr)
    for i in range (1, n):
        value = arr[i]
        hole = i
        while (hole > 0 and arr[hole - 1] > value):
            arr[hole] = arr[hole - 1]
            hole -= 1
        
        arr[hole] = value

'''
Merge two sorted arrays 
given two sorted arrays, need to mege these two arrays 
naive approach  time complexity: O(nlogn(n))
'''
def merge_array(a, b):
    res = a + b
    res.sort()

    return res 

# optimize merge sort two arrays 
def merge_array_optimized(a, b):
    res = []
    m = len(a)
    n = len(b)
    i = j = 0

    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    
    while i < m:
        res.append(a[i])
        i += 1
    
    while j < n:
        res.append(b[j])
        j += 1

    return res 
'''
merge sort: very efficient sorting algorithm
based on divide and conquer approach
merge() takes O(n) time 
merge_sort() takes O(log2n) so combined :-
O(nlogn) is the best possible worst-case runtime 
'''
def merge(left, right):

    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left
    
    result = [] 
    left_indx = right_indx = 0

    while len(result) < ( len(left) + len(right)):

        if left[left_indx] <= right[right_indx]:
            result.append(left[left_indx])
            left_indx += 1
        else:
            result.append(right[right_indx])
            right_indx += 1
        
        if len(left) == left_indx:
            result += right[right_indx:]
            break

        if len(right) == right_indx:
            result += left[left_indx:]
            break

    return result 

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2

    return merge(left=merge_sort(arr[:mid]),
                right=merge_sort(arr[mid:])) 


'''
Union of two sorted lists 
eg: I/P a = [3, 5, 8] 
b = [2, 8, 9]
O/P: [2, 3, 5, 8, 9]
naive solution
Efficient solution using merge(left, right)
print distinct element using list(set(merge()))
'''
def union_list(a, b):
    result = a + b
    result.sort()
    

    return list(set(result))

'''
intersection of two lists 
built in intersection: Sets is implemented efficiently using hash tables 
allows for constant time average-case performance
worst case could approach O(n) where n is the size of the larger set 
overall time complexity of below function: O(min(len(a), len(b)))
'''
def intersection_list(a, b):
    result = set(a).intersection(b)

    return result 

'''
overall intersection_list and .._sol2 have same time complexity
however if there are many common elements between the lsits
sol2 implementation can be more efficient than the set intersection approach
especially if the lists are already sorted 
'''
def intersection_list_sol2(a, b):
    m = len(a)
    n = len(b)
    i = j = 0
    result = []
    while i < m and j < n:
        if i > 0 and a[i - 1] == a[i]:
            i += 1
            continue 

        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        
        else:
            result.append(a[i])
            i += 1
            j += 1
    
    return result

'''
Inversion: A pair (arr[i], arr[j]) forms an inversion when 
i < j and arr[i] > arr[j]
naive approcah: O(n^2)
efficient solution using merge sort: nlogn time complexity 
'''
def count_inversion(arr):
    count = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if i < j and arr[i] > arr[j]:
                count +=1
    
    return count 

#modified merge sort to count inversion 
# O(nlogn)
def merge_to_count(left, right):
    inversions = 0  # Counter for inversions
    if len(left) == 0:
        return right, inversions
    
    if len(right) == 0:
        return left, inversions
    
    result = [] 
    left_indx = right_indx = 0

    while len(result) < (len(left) + len(right)):

        if left[left_indx] <= right[right_indx]:
            result.append(left[left_indx])
            left_indx += 1
        else:
            result.append(right[right_indx])
            right_indx += 1
            inversions += len(left) - left_indx  # Increment inversions count

        if len(left) == left_indx:
            result += right[right_indx:]
            break

        if len(right) == right_indx:
            result += left[left_indx:]
            break

    return result, inversions

def merge_sort_to_count(arr):
    if len(arr) < 2:
        return arr, 0
    
    mid = len(arr) // 2

    left, left_inversions = merge_sort_to_count(arr[:mid])
    right, right_inversions = merge_sort_to_count(arr[mid:])
    
    merged_arr, merge_inversions = merge_to_count(left, right)
    
    total_inversions = left_inversions + right_inversions + merge_inversions

    return merged_arr, total_inversions

# partition list, naive solution: theta(n)
def list_partition(arr, pivot):
    n = len(arr)
    arr[pivot], arr[n-1] = arr[n-1], arr[pivot]
    temp = []
    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)
    
    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
    
    for i in range(n):
        arr[i] = temp[i]
    
    return arr

'''
Lomuto partition :linear time
takes only one traversal theta(1) auxiliary space 
'''
def lomuto_partition(arr, start, high):

    pivot = arr[high]
    i = start - 1
    for j in range(start, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    #returns the index of pivot in corret position
    return i+1

'''
Hoare's partition: linear time theta(1) space 
faster than lomuto partition 
constants are smaller than lomuto 
first element as pivot 
there's no guarantee that pivot goes to correct positon
'''
def hoare_partition(arr, start, high):

    pivot = arr[start]
    i = start - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

''''
Quick Sort : Divide and conquer algorithm
worst case time :O(n^2) despite this it is considered faster because:
In-placa, cache friendly, average case in O(nlogn), tail recursivve 
'''
def quicksort_hoarse(arr, l, h):
    if l < h:
        p = hoare_partition(arr, l, h)
        quicksort_hoarse(arr, l ,p)
        quicksort_hoarse(arr, p + 1, h)

def quicksort_lomuto(arr, l, h):
    if l < h:
        p = lomuto_partition(arr, l, h)
        quicksort_lomuto(arr, l ,p - 1)
        quicksort_lomuto(arr, p + 1, h)


def main():
    test_arr = [10, 8, 20, 5]
    #bubble_sort_optimized(test_arr)
    #selection_sort(test_arr)
    #insertion_sort(test_arr)
    #merge_sort(test_arr)
    # a = [2, 3, 3, 3]
    # b = [3, 4, 4]
    # print(intersection_list_sol2(a,b))
    test_arr1 = [8, 4, 7, 9, 3, 10, 5]
    quicksort_lomuto(test_arr1, 0, 6)
    print(*test_arr1)
    


if __name__ == "__main__":
    main()