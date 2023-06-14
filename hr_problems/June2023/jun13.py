#Set Mutations 

def mutation_operations(elements_in_A, number_of_operations):
    for i in range(0, number_of_operations):
        operation_name = input().split()
        another_set = set(map(int, input().split(' ')))

        if operation_name[0] == 'intersection_update':
            elements_in_A.intersection_update(another_set)
        
        elif operation_name[0] == 'update':
            elements_in_A.update(another_set)

        elif operation_name[0] == 'symmetric_difference':
            elements_in_A.symmetric_difference(another_set)
        
        else:
            elements_in_A.difference_update(another_set)
    
    print(sum(elements_in_A))

def main():
    number_in_A = int(input())
    elements_in_A = set(map(int, input().split(' ')[:number_in_A]))

    number_of_operations = int(input())
    mutation_operations(elements_in_A, number_of_operations)


if __name__ == '__main__':
    main()