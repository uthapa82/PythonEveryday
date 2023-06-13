def main():
    m = int(input())
    value_m = list(map(int, input().split(' ')[:m]))
    
    n = int(input())
    value_n = list(map(int, input().split(' ')[:n]))

    myset_m = set(value_m)
    myset_n = set(value_n)
    
    result_1 = myset_m.difference(myset_n)
    result_2 = myset_n.difference(myset_m)
    final_set = set(list(result_1) + list(result_2))
    
    for element in sorted(final_set):
        print(element)

def alternate_sol():
    m = input()
    set_m = set(map(int, input().split()))
    
    n = input()
    set_n = set(map(int, input().split()))
    
    res_1 = set_m.difference(set_n)
    res_2 = set_n.difference(set_m)
    
    for element in sorted(res_2.union(res_1)):
        print(element)
        
if __name__ == '__main__':
    main()
    alternate_sol()