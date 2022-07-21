# gfg fork python Nearest Problem Contest 1
# You are given two numbers A and B. When A is raised to some power P, we get a
# number X. What value of X that is closet to B
import math

def nearestPower(A, B):
    result = math.floor(math.log(B, A))
    newResult = result + 1
    result1 = A ** result
    result2 = A ** newResult
    if(abs(result1 - B) > abs(result2 - B)):
        return result2
    else:
        return result1
    
def main():
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    result = nearestPower(A, B)
    print("The result is: ", result)
    
if __name__ == "__main__":
    main()