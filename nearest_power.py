# gfg fork python Nearest Problem Contest 1
# You are given two numbers A and B. When A is raised to some power P, we get a
# number X. What value of X that is closet to B
import itertools

def nearestPower(A, B):
    result = 1
    while True:
        result *= A
        if result > B:
            return int(result/A)
    # for i in range(1, B):
    #     if pow(A, i) <= B:
    #         result = pow(A, i)
    #         break
    #     else:
    #         continue
            
    return int(result)
    
def main():
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    result = nearestPower(A, B)
    print("The result is: ", result)
    
if __name__ == "__main__":
    main()