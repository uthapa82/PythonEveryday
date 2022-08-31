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
    
# animal cracker 
def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)

    return wordlist[0][0] == wordlist[1][0]

#makes twenty 
def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        return True
    
    elif n1 == 20:
        return True
    
    elif n2 == 20:
        return True
    
    else:
        return False
        
def main():
    print(lesser_of_two_evens(2, 4))
    print(lesser_of_two_evens(2, 5))
    
    #better solution
    print("\nEfficient Solution: ")
    print(better_soluton(2, 4))
    print(better_soluton(2, 5))
    
    # Animal Cracker
    print("\nAnimal Cracker: ")
    print(animal_crackers('Levelheaded Llama'))
    
    # makes twenty problem
    print("\nMakes Twenty Problem: ")
    print(makes_twenty(10, 10))
    

if __name__ == "__main__":
    main()