
#a.symmetric_difference(B) or A^B

def symmetricDiff(eng_paper, fren_paper):

    result = eng_paper.symmetric_difference(fren_paper)
    print(len(result))

def main():
    english_paper = int(input())
    eng_student_roll = list(map(int, input().split(' ')[:english_paper]))
    
    french_paper = int(input())
    fren_student_roll = list(map(int, input().split(' ')[:french_paper]))

    eng_set =  set(eng_student_roll)
    fren_set = set(fren_student_roll)

    #function call 
    symmetricDiff(eng_set, fren_set)

if __name__ == '__main__':
    main()
