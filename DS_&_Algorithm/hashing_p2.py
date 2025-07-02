def count_pairs_with_sum(arr, target):
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            return 1
        seen.add(num)
    
    return 0

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 14
    print(count_pairs_with_sum(arr, target))

if __name__ == "__main__":
    main()