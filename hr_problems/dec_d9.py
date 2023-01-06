from itertools import combinations_with_replacement as cr

def main():
    user_word = input("Enter the word and r value: ").split()
    result = cr(sorted(user_word[0]), int(user_word[1]))
        
    for item in result:
        print("".join(item))

if __name__ == '__main__':
    main()