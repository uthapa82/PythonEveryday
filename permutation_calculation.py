from itertools import combinations, permutations

def using_module():
    perm = permutations([1, 2, 3], 2)
    print("Permutation")
    for i in list(perm):
        print(i)
    
    comb = combinations([1, 2, 3], 2)
    print("Combination")
    for j in list(comb):
        print(j)
           
def main():
    using_module()
    
if __name__ == '__main__':
    main()