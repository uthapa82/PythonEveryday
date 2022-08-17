# GFG contest fork python 
def mean(D, M):
    newSum = (3 * M) + D
    newMean = newSum/4
    return int(newMean)
    
def main():
    D = int(input())
    M = int(input())
    result = mean(D, M)
    print(result)
    
if __name__ == "__main__":
    main()