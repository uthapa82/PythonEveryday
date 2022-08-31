def lesser_of_two_evens(a, b):
    if a%2 == 0 and b%2 == 0:
        #both are even
        if a < b:
            result = a
        else:
            result = b
    else:
        # one or both numbers are odd
        if a > b:
            result = a
        else:
            result = b 
    return result 

def better_soluton(a, b):
    if a%2 == 0 and b%2 == 0:
        return min(a, b)
    else:
        return max(a, b)
     
def main():
    print(lesser_of_two_evens(2, 4))
    print(lesser_of_two_evens(2, 5))
    
    #better solution
    print("\nEfficient Solution: ")
    print(better_soluton(2, 4))
    print(better_soluton(2, 5))

if __name__ == "__main__":
    main()