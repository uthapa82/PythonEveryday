# binary search Recursive 

def binary_search(arr, low, high, value):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == value:
            return mid
        
        elif arr[mid] > value:
            return binary_search(arr, low, mid - 1, value)
        
        else:
            return binary_search(arr, low + 1, high, value)
    
    else:
        return -1

def main():
    test_array = [2, 3, 4, 10, 40]
    find_value = 10
    
    result = binary_search(test_array, 0, len(test_array)-1, find_value)

    if result != -1:
        print(f"Value {find_value} found at index", str(result))

    else:
        print(f"Value {find_value} not present")

if __name__ == "__main__":
    main()