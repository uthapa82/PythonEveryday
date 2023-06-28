# strict superset 

def main():
    elements_of_A = set(map(int, input().split()))
    final_set = set()

    for number in range(int(input())):
        other_set = map(int, input().split())
        final_set.update(other_set)
    
    print(elements_of_A.issuperset(final_set))

if __name__ == '__main__':
    main()