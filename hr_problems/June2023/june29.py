# zip([iterable,...])
# function returns a list of tuples 

def main():
    N, X = map(int, input().split())
    final_scores = []
    
    for i in range(X):
        scores = map(float, input().split())
        final_scores.append(scores)

    temp_zip = list(zip(*final_scores))
    
    for j in temp_zip:
        print(round(sum(j)/X, 2))

if __name__ == '__main__':
    main()