from collections import namedtuple
def main():
    total_students = int(input('Total Students: '))
    Scores = namedtuple('Scores', input())
    sum = 0
    for marks in range(total_students):
        student = Scores(*input().split())
        sum += int(student.MARKS)
        
    average = sum / total_students
    print(average)
    
if __name__ == '__main__':
    main()