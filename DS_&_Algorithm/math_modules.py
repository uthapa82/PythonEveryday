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

# time complexity theta(axb - max(a, b))
def lcm(a, b):
    res = max(a, b)

    while True:

        if res % a == 0 and res % b == 0:
            return res 
        
        res += 1
    
    return res

def optimal_lcm(a, b):

    return a * b // gcd_optimal(a, b)

# Time --> O(sqrt(n))
def is_prime(n):
    if n == 1:
        return False 
    
    i = 2 
    while (i * i <= n):

        if n % i == 0:
            return False 
        
        i += 1

    return True 

# 3 x is_prime(n)
def is_prime_optimization(n):
    if n == 1:
        return False 
    
    if n == 2 or n == 3:
        return True
    
    if  n == 2 or n == 3:
        return True 
    
    if n % 2 == 0 or n % 3 == 0:
        return False 
    
    i = 5
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False 
        
        i += 6
    
    return True 