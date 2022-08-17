# Print a list in reverse order(from last to first item) using while and for in loops.

def reverse_list(list):
    resultList = []
    for i in list:
        # insert(index/position, element)
        resultList.insert(-i, i)
        
    return resultList


def main():
    sample_list = [1,2,3,4]
    print(reverse_list(sample_list))
    
if __name__ == "__main__":
    main()