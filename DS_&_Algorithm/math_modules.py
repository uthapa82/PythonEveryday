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

    #alternate solution 
    # O(log5n)
    while (n / i >= 1):
        res += int(n / i)
        i *= 5
    return int(res)

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

# O(log(min(a,b)) as we are using euclidean algorithm for gcd 
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
    if n <= 1:
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
# efficient solution
# time complexity O(sqrt(n)) 
def prime_factor_efficient(n):
    while n % 2 == 0:
        print(2)
        n /= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            print(i)
            n /= i
    
    if n > 2:
        print(n)
    
#efficient solution, print all divisors but not in order 
# time : O(sqrt(n)), aux Space: O(1) 
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
    
    # [True for i in range(n+1)]
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

# optimized version using Stirling's approximation formula 
# time complexity is optimized to constant time from linear logarithmic (nlogn)
def opt_digit_count_fact(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    
    result = (n * math.log10(n/math.e) + math.log10(2 * math.pi * n) / 2.0)
    
    return math.floor(result) + 1

# time complexity = O(1)
def absolute_value(n):
    if n <= 0:
        return n * -1
    
    return n

# time complexity = O(N)
def fact_number_rec(n):
    if n == 0 or n == 1:
        return 1
    
    return (n * fact_number_rec(n - 1))

# finding perfect square 
# time complexity = O(N ^1/2 * N^1/4)
def exactly_divisors(n):
    if n < 3:
        return 0
    
    count = 0 
    i = 2
    while(i * i <= n):
        if(is_prime_optimization(i)):
            count += 1
        i += 1
    
    return count 

# quadratic equation
# time complexity O(1) 
def quadratic_roots(a, b, c):
    determinant = (b ** 2) - (4 * a * c)
    if determinant > 0:
        root1 = math.floor((-b + math.sqrt(determinant))/(2 * a))
        root2 = math.floor((-b - math.sqrt(determinant))/(2 * a))

    elif determinant == 0:
        root1 = math.floor(-b / (2 * a))
        root2 = root1

    else:
        return [-1]
    
    if root1 > root2:
        return [root1, root2]
    else:
        return [root2, root1]

# time complexity O(logn)    
def geometric_series(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return b 
    else:
        return (a * math.pow((b/a), (n - 1)))

# computing power
# Time complexity = O(n) 
def power(x , n):
    if (n == 0):
        return 1
    
    if (x == 0):
        return 0
    
    return x * power(x, n - 1)
'''
list/dictionary/set/Generator comprehensions 
output_list = [output_exp for var in input_list if (var satisfies this condition)]
eg. [var for var in input_list if var % 2 == 0]

output_dict = {key:value for (key,value) in iterable if (key, value satisfy this condition)}
eg. {var:var **3 for var in input_list if var % 2 != 0}

output_set = {var for var in input_list if var % 2 == 0}
    - very similar to list only difference is set use curly brackets 

generator_output = (var  for var in input_list if var % 2 == 0)
for var in generator_output:
    print(var, end = ' ')

    - very similar to list comprehensions one difference is that generator use small brackets (wheras list - [])
    - also generator don't allocate memory for the whole list, instead they generate each value one by one , more 
    memory efficient 
'''

# array second largest element in a list 
# time complexity : O(n)
def max_second(arr, arr_size):
    if arr_size < 2:
        print("Invalid Input: ")
        return
    
    first = second = -2147483648
    for i in range(arr_size):
        if (arr[i] > first):
            second = first 
            first = arr[i]

        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
        
    if (second == -2147483648):
        print("No second largest element")
    else: 
        print("Second largest element is ", second)

# check if the list is sorted - O(n)
def is_sorted(lst, arr_len):
    if (arr_len == 0 or arr_len == 1):
        return True
    
    for i in range(1, arr_len):
        if (lst[i-1] > lst[i]):
            return False
    
    return True



