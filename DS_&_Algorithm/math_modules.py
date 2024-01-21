#various mathematical functions 
# trailing zeros in factorial 
import math

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
    
    if n % 2 == 0 or n % 3 == 0:
        return False 
    
    i = 5
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False 
        
        i += 6
    
    return True 

# prime factorization 
# naive solution 
def prime_factor(n):
    for i in range(2, n+1):
        if is_prime_optimization(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i

#efficient solution, print all divisors but not in order 
# time : theta(n^1/2), aux Space: O(1) 
def print_divisor(n):
    i = 1
    while(i*i <= n):
        if(n%i == 0):
            print(i)
            if (i != n/i):
                print(n//i)
        i += 1

# sorted, theta(sqrt(n))
def print_divisor_sort(n):
    i = 1
    while(i*i < n):
        if(n%i == 0):
            print(i)
        i += 1
    
    while(i >= 1):
        if(n%i == 0):
            print(n//i)
        i -= 1

#Sieve of Eratosthenes 
def sieve(n):
    if n <= 1:
        return
    
    prime_number = [True] * (n+1)

    i = 2


    while(i*i <= n):
        if prime_number[i]:
            for j in range(2 * i, n+1, i):
                prime_number[j] = False
        i += 1
    
    for i in range(2, n + 1):
        if prime_number[i]:
            print(i, end = " ")

#O(n loglog n) => we can say linear 
def sieve_optimized(n):
    if n <= 1:
        return
    prime_number = [True] * (n+1)

    i = 2
    while i <= n:
        if prime_number[i]:
            print(i, end = " ")

            for j in range(i*i, n+1, i):
                prime_number[j] = False
        
        i += 1

#finding the digits in a factorial of n
# log(a*b) = log(a) + log(b)
# log( n!) = log(1*2*3...*n) = log(1) + log(2) + ... + log(n)
# Time complexity: O(N log N)
def digits_in_fact(n):
    #factorial exists only for n >= 0
    if (n < 0):
        return 0
    
    # base case 
    if (n <= 1):
        return 1
    
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)
    
    return math.floor(digits) + 1
    
