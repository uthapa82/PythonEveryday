# intersection operator 

def main():
    no_of_students_eng = int(input("Enter the number of students (English): "))
    my_set_eng = set(map(int, input().split(' ')[:no_of_students_eng]))
    
    no_of_students_fren = int(input("Enter the number of French Subscriber: "))
    my_set_fren = set(map(int, input().split(' ')[:no_of_students_fren]))
    
    print(len(my_set_eng.intersection(my_set_fren)))

if __name__ == '__main__':
    main()