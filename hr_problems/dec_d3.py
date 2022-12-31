# permutations are printed in a lexicographic sorted order 
from itertools import permutations

def main():
    user_word = input("Enter the word and r value: ").split()
    result = permutations(user_word[0], int(user_word[1]))
    
    for item in sorted(result):
        print("".join(item))

if __name__ == '__main__':
    main()