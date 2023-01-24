def set_difference():
    no_of_students_eng = int(input())
    my_set_eng = set(map(int, input().split(' ')[:no_of_students_eng]))
    
    no_of_students_fren = int(input())
    my_set_fren = set(map(int, input().split(' ')[:no_of_students_fren]))
    
    print(len(my_set_eng.difference(my_set_fren)))

def main():
    a = int(input('Enter number a: '))
    b = int(input('Enter number b: '))
    m = int(input('Enter number m: '))
    
    print(pow(a, b))
    print(pow(a, b, m))
    
if __name__ == '__main__':
    set_difference()