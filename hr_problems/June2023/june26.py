#subset 

def main():
    test_cases = int(input())
    for element in range(test_cases):
        elements_in_A = int(input())
        set_A = set(map(int, input().split()[:elements_in_A]))
        
        elements_in_B = int(input())
        set_B = set(map(int, input().split()[:elements_in_B]))

        if set_A.issubset(set_B):
            print("True")
        else:
            print("False")



if __name__ == '__main__':
    main()