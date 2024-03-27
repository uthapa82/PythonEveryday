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
        
def main():
    test_arr = [10, 8, 20, 5]
    bubble_sort_optimized(test_arr)
    print(*test_arr)

if __name__ == "__main__":
    main()