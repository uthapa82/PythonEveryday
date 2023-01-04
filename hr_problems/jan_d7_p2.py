from itertools import combinations

def main():
    user_word = input("Enter the word and r value: ").split()
    result = combinations(sorted(user_word[0]), int(user_word[1]))
    
    for letter in sorted(''.join(user_word[0].split())):
        print(letter)
        
    for item in result:
        print("".join(item))
        
       
if __name__ == '__main__':
    main()
