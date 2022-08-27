
def repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
                
    return repeated

def counter():
    list_2 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    new = []
    for a in list_2:
        n = list_2.count(a)
        if n > 1:
            if new.count(a) == 0:
                new.append(a)
    print(new)

def main():
    list_1 = [10, 20, 30, 20, 30, 40, 50, -20, 60, -20]
    print("Brute Force Approach ")
    print(repeat(list_1))
    
    counter()
    
    
if __name__ == "__main__":
    main()