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

    * $ C < loglogn < logn < n^{1 \over 3} < n^{1 \over 2} < n <n^2 < n^3 < n^4 < 2^n < n^n $ 

    * constant is lowest growing thing then loglogn grows faster than constant ........

    * Example :
    $f(n)= 2n^2 + n + 6$
    $g(n) = 100n + 3$
    * ignore lower order : n from f(n) and ignore constant 3 , 6, 2 and 100
    * The remaining is n^2 and n so n is faster, therefore g(n) is faster than f(n)

**Big O Notation**
* Upper Bound in Order of Growth 
* we say $f(n) = O(g(n))$ iff there exists constant C and n0 such that $f(n) \leq Cg(n)$ for all $n \geq n0$
* constant, lower order notation doesn't matter 
* ignore lower order notation, ignore the constant 

<br>

* ${n \over 4}, 2n+3, {n \over 100} + logn, n+1000, {n \over 10000}, logn+100$   belongs to O(n)

<br>

* ${n^2 \over 4}, 2n^2+3, {n^2 \over 100} + logn, n^2+1000, {n^2 \over 10000}$    belongs to O(n)

**Omega Notation- Lower Bound**
*  $f(n) = \Omega(g(n))$ iff there exist positive constants c and $n_0$ such that $0 \leq cg(n) \leq f(n)$ for all $n \geq n_0$
* if $f(n) = \Omega (g(n))$ then $g(n) = O(f(n))$
* Omega notation is useful when we have lower bound on time complexity 

**Theta Notation -Exact bound**
* $f(n) = \theta (g(n))$ iff there exist constants $C_1, C_2$ (where $C_1 > 0$ and $C_2 >0$) and $n_0$ (where $n_0 \geq 0$) such that $C_1g(n) \leq f(n) \leq C_2g(n)$ for all $n \geq n_0$

**Analysis of Recursion**
* Recursion Tree Method 
    - we write non-recursive part as root of tree and recursive parts as children 
    - we keep expanding children until we see a pattern 

**Space Complexity**
* Order of growth of memory(or RAM) usage in terms of input 
* Auxiliary space : order of growth of extra space(space other than input/output)

```
    #src: gfg 
    def search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
    return -1
```
* **Worst Case Analysis (Usually Done)**: In the worst case analysis, we calculate upper bound on running time of an algorithm. We must know the case that causes the maximum number of operations to be executed. For Linear Search, the worst case happens when the element to be searched (x in the above code) is not present in the array. When x is not present, the search() functions compares it with all the elements of arr[] one by one. Therefore, the worst case time complexity of linear search would be  O(N), where N is the number of elements in the array

* **Average Case Analysis (Sometimes done)**:  In average case analysis, we take all possible inputs and calculate computing time for all of the inputs. Sum all the calculated values and divide the sum by total number of inputs. We must know (or predict) distribution of cases. For the linear search problem, let us assume that all cases are uniformly distributed (including the case of x not being present in array). So we sum all the cases and divide the sum by (N+1). Following is the value of average case time complexity..

* **Best Case Analysis (Bogus)**: In the best case analysis, we calculate lower bound on running time of an algorithm. We must know the case that causes minimum number of operations to be executed. In the linear search problem, the best case occurs when x is present at the first location. The number of operations in the best case is constant (not dependent on N). So time complexity in the best case would be O(1)

* **Auxiliary Space** : The extra space or temporary space used by an algorithm 

* **Space Complexity**: The total space taken by the algorithm with respect to the input size.

### Sorting 
* The worst case of QuickSort occurs when the picked pivot is always one of the corner elements in sorted array, in worst case, quicksort recursively calls one subproblem with size 0 and other subproblem with size (n-1). So recurrence is 

    $T(n) + T(n-1) + O(n)$ 

    which can be rewritten as 

    $T(n) = T(n-1) + O(n)$

* If we use the median as a pivot element, then the recurrence for all cases becomes 

    $T(n) = 2T(n/2) + O(n) $

    The above recurrence can be solved using master method. It falls in case 2 of the master method.

    So, the worst-case the worst case time complexity of this modified Quick Sort is O(nLogn)

* QuickSort is not a stable sorting algorithm in its typical implementation 

* Insertion sort takes linear time when input array is sorted or almost sorted (maximum 1 or 2 elements are misplaced). All other sorting algorithms mentioned above will take more than linear time in their typical implementation 

* Given an unsorted array , that every element in the array is at most k distance from its position in a sorted array where k is a positive integer smaller than the size of an array, which sorting algorithm can be easily modified for sorting this array and what is obtainable time complexity ? 

    * We can perform in O(nlogK) time using heaps 
    * first create a min-heap with first k+1 elements. Now we are sure that the smallest element will be in this K + 1 element. Now, remove the smallest element from the min-heap(which is the root) and put it in the result array. Next, insert another element from the unsorted array into the mean-hip, now the second smallest element will be in this.Extract it from the mean-heap and continue this until no more elements are in the unsorted array. Next, use a simple heap sort for the remaining elements 

    **Time Complexity**
    O(K) to build the initial min-heap 
    O((n-k)logk) for remaining elements 

    Thus we get O(nlogk)

* In a situation where swap operation is very costly, selection sort should be pregerred as it makes 
O(n) swaps which is the minimum among all sorting algorithms like insertion, merge, heap sort 

* Suppose we are sorting an array of eight integers using quicksort, and we have just finished the first partitioning with the array looks like :
    `2 5 1 7 9 12 11 10`

    in this case the povot could be either 7 or 9 as all the elements on the left of 7 and 9 are smaller than 7 and 9 respectively and on right are greater than 7 and 0 respectively 

* Suppose we are sorting an array of eight integers using heapsort, and we have just finished some heapify (either maxheapify or minheapify) operations. The array now looks like this: 16 14 15 10 12 27 28 How many heapify operations have been performed on root of heap? => 2 ,In Heapsort, we first build a heap, then we do following operations till the heap size becomes 1 
    * Swap the root with last element 
    * Call heapify for root 
    * reduce the heap size by 1 