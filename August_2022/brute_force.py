
def repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
                
    return repeated

def main():
    list_1 = [10, 20, 30, 20, 30, 40, 50, -20, 60, -20]
    print("Brute Force Approach ")
    print(repeat(list_1))
    
    
if __name__ == "__main__":
    main()