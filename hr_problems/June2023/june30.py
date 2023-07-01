# eval() expression 
# any() expression returns True if any element of the iterable is true 

def main():
    N = int(input())
    number_n = list(map(int, input().split()[:N]))
    if all(num > 0 for num in number_n) and any((str(word) == str(word)[::-1]) for word in number_n):
        print("True")
    
    else :
        print("False")

if __name__ == '__main__':
    main()