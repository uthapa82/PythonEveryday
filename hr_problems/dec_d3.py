# permutations are printed in a lexicographic sorted order 
# A set is an unordered collection of elements without duplicate entries 

from itertools import permutations

def main():
    user_word = input("Enter the word and r value: ").split()
    result = permutations(user_word[0], int(user_word[1]))
    
    for item in sorted(result):
        print("".join(item))

def average(array):
    distinct_heights = set(array)
    new_total_number = len(distinct_heights)
    final_result = sum(distinct_heights) / new_total_number
    
    return final_result

if __name__ == '__main__':
    main()
    n = int(input("Enter the array size: "))
    arr = list(map(int, input("Enter elements in array(space separated) : ").split()))
    result = average(arr)
    print(result)