from itertools import combinations

def main():
    user_word = input("Enter the word and r value: ").split()
    result = combinations(sorted(user_word[0]), int(user_word[1]))
    
    for letter in sorted(''.join(user_word[0].split())):
        print(letter)
        
    for item in result:
        print("".join(item))
        
def alternate_sol():
    s, k = input().split()
    for i in range(1, int(k)+1):
        for j in combinations(sorted(s), i):
            print(*j, sep='')  
             
if __name__ == '__main__':
    #main()
    alternate_sol()
