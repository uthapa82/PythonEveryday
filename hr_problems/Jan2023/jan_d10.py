from collections import deque

def main():
    no_of_commands = int(input("Enter the number of input: "))
    dq = deque()

    for i in range(no_of_commands):
        command = input().split()
        if command[0] == 'pop':
            dq.pop()
            
        elif command[0] == 'append':
            dq.append(int(command[1]))
        
        elif command[0] == 'appendleft':
            dq.appendleft(int(command[0]))
            
        else:
            dq.popleft()

    print(*dq)
    
if __name__ == '__main__':
    main()