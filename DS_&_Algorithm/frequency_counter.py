# Naive solution O(n^2)
def arr_frequencies(arr, n):
    
    for i in range(n):
        flag = False 
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True
                break
        
        if flag == True:
            continue
        freq = 1 

        for j in range (i + 1, n):
            if arr[i] == arr[j]:
                freq += 1
        
        print(arr[i], freq)

# dictionary use: O(n) 
def arr_frequencies_2(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    for element, count in frequency.items():
        print(f"{element} {count}")
        

def main():
    test_arr = [10, 20, 20, 30, 10]
    arr_frequencies(test_arr, len(test_arr))
    arr_frequencies_2(test_arr)

if __name__ == "__main__":
    main()