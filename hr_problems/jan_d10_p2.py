
def main():
    no_of_commands_eng = int(input("Enter the number of input for set A: "))
    my_set_eng = set(map(int, input().split(' ')[:no_of_commands_eng]))
    
    no_of_commands_french = int(input("Enter the number of input for set B: "))
    my_set_french = set(map(int, input().split(' ')[:no_of_commands_french]))
    
    result = my_set_eng.union(my_set_french)
    print(len(result))
    
if __name__ == '__main__':
    main()