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
given two sorted arrays, need to meger these two arrays 
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


def main():
    test_arr = [10, 8, 20, 5]
    #bubble_sort_optimized(test_arr)
    #selection_sort(test_arr)
    #insertion_sort(test_arr)


if __name__ == "__main__":
    main()