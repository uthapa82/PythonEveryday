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

def main():
    print(lesser_of_two_evens(2, 4))
    print(lesser_of_two_evens(2, 5))

if __name__ == "__main__":
    main()