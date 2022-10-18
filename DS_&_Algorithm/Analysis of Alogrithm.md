### Analysis of Algorithms (Background)
* Sum of n natural numbers :
    * Input : n = 3
    * Output: 6 // 1 + 2 + 3
    * Input: n = 5
    * output: 15 // 1 + 2 + 3 + 4 + 5

```
def sum_sol_1(n):
    return n*(n+1)/2

def sum_sol_2(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def sum_sol_3(n):
    result = 0
    for i in range(1, n+1):
        for j in range(1, i+j)
            result = result + 1
    return result


```

**Asymptotic Analysis: (Theoritical Analysis)**
* No dependency on machines, programming language etc
* We do not have to implement all ideas/algorithms
* Asymptotic analysis is about measuring order of growth in terms of input size.

* *write pseudocode and analyze algorithm*

**Order of Growth**
* Constant -> sum_sol_1()
* c2*n + c3 --> sum_sol_2()----> linear 
* c4 * n^2 + c5 * n + c6 --> sum_sol_3()---> quadratic 

<br>

* A function f(n) is said to be growing faster than g(n) if 

    * $\displaystyle{\lim_{n \to \infty}} {f(n) \over g(n)}$  = ${\infty}$


    *  $\displaystyle{\lim_{n \to \infty}} {g(n) \over g(n)}$  = ${0}$

<br>

* Direct Way :
1. Ignore lower order terms 
2. Ignore leading constant 

    * $ C < loglogn < logn < n^{1 \over 3} < n^{1 \over 2} < n <n^2 < n^3 < n^4 < 2^n < n^n$ 

    * constant is lowest growing thing then loglogn grows faster than constant ........

    * Example :
    $f(n)= 2n^2 + n + 6 $
    $g(n) = 100n + 3$
    * ignore lower order : n from f(n) and ignore constant 3 , 6, 2 and 100
    * The remaining is n^2 and n so n is faster, therefore g(n) is faster than f(n)

**Best, Average and Worst Cases**

```
def get_sum_odd(l):
    if len(l) % 2 == 0;
        return 0
    sum = 0
    for x in l:
        sum = sum + x 
    return sum 

```
* we cannot make any general statement about the code above for order of growth because sometimes it is going to take the constant time ==> if the number of elements are even, if it have odd number elements then it's going to take linear time 

* In the scenario above we divide algorithm into threee cases 
    1. Best Case 
        * Constant 
    2. Average Case 
        * Linear (*under assumption that even and odd cases are equally likely*)

    3. Worst Case 
        * Linear 

**Assymptotic Notation**
* Big O: Represents exact or upper bound 
    * $O(n), O(n^2)$

* Theta : Represents exact bound
    * for $C1n + C2 $,  we have to write as $\theta(n)$

* Omega: Represents exact or lower bound 
    * $\omega(n), \omega(1), \omega(logn)$

**Big O Notation (Upper Bound on Order of Growth)**
* we say $f(n) = O(g(n))$ iff there exist constants C and n~0~ such that $f(n) \leq Cg(n)$ for all $n \geq n_0$

