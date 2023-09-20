#various mathematical functions 
# trailing zeros in factorial 


def trail_zero(value):
    #Naive problem 
    # not optimal solution 
    fact = 1
    for i in range(2, value + 1):
        fact = fact * i 
    res = 0

    while(fact % 10 == 0):
        res += 1
        fact = fact // 10
    return res 

    #-------Efficient Solution -----
    # Time: theta(logn), aux space:O(1) 
    res = 0
    i = 5
    while(i <= value):
        res = res + (value // i)
        i = i * 5
    return res 

#GCD Euclidean Algorithm 
#  time complexity O(min(a, b))
def gcd(A, B):
    while A != B:
        if A > B:
            A = A- B
        else: 
            B = B - A 
    return A

def gcd_optimal(A, B):
    if B == 0:
        return A
    
    return gcd(B, A % B)
