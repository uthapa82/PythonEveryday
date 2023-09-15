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