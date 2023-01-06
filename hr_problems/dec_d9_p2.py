def main():
    no_of_elements = int(input("Enter the number of elements in the set : "))
    my_set = set(map(int, input().split(' ')[:no_of_elements]))
    
    no_of_commands = int(input("Enter the number of commands: "))
    for i in range(no_of_commands):
        command = input().split()
        if command[0] == 'pop':
            my_set.pop()
            
        elif command[0] == 'remove':
            my_set.remove(int(command[1]))
            
        else:
            my_set.discard(int(command[1]))      

    print(sum(my_set))
    
if __name__ == '__main__':
    main()