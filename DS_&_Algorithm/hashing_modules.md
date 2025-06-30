**Introduction**
- Hashing  Search/Insert/Delete ---> O(1) an average 
- Efficient than array, avial tree, red black tree.
- However it doesn't provide certain operations that others provide 
- Not useful for:
    - finding closet value ---> Tree (AVL/Red Black Tree)
    - Sorted Data  ---> Tree (AVL/Red Black Tree)
    - Prefix Search ---> Trie 
    
**Hashing Application**
After Array second most used Datastructure in Computer Science 
- Dictionaries 
    - Implementing dictionaries using hashing, can perform lookup in constant time 
- Database Indexing 
    - primary/seconday indexing, implemented us B/B+ trees or hashing 
- Cryptography 
    - stored password in webpages using hashing
- Caches 
    - URL -> key Data -> value : quickly search for the local file 
- Symbol Tables in Compilers/Interpreters 
- Routers 
- Getting data from databases  
    
**Direct Address Table**
Use keys as indexes in an array 
Imagine a situation where we have 1000 keys with values from (0 to 999), how would we implement O(n) time :
    1. Search 
    2. Insert 
    3. Delete
    Example operations:
        insert (10), insert(20), insert(119), search(10), search(20), delete(119), search(119)
    - works only where keys are small , doesn't work if keys have large values eg. phone, float (cost of someting), string values( addresses)

**Hashing**
- take large universe of keys (eg. phone numbers, names, employee ID) ---> Hash Function ---> convert to small values [0 | 1 .......| m-1 ] i.e Hash tables 
- How hash functions work ? 
    - should always map a large key to same small key 
    - should generate values from 0 to m-1 
    - should be fast, O(1) for integer and O(len) for string of length "len"
    - **should uniformly distribute larger keys into hash table slots**

*Example Hash Functions*

    1. h(large_key) = large_key % m

    2. For strings, weighted sum  `str[] = "abcd"

        str[0] * $ x^0  + str[1] * x^1 + str[2] * x^2 + str[3] * x^4 $

    3. Universal Hashing 

**Collision Handling**
- If we know keys in advance, then we can perfect hashing (guarantees no collision)
- If we do not know keys, then we use on of the following
    - Chaining
    - Open Addressing
        - Linear Probing
        - Quadratic Probing
        - Double Hashing
    
- Birthday Paradox => 23 people in room , probability that 2 people might have same birthday chance--> 50% , for 70 people probability = 99.9%

**Chanining**
- miaintain array of linkedin list headers 

Example 
- hash(key) = key % 7
- keys = {50, 21, 58, 17, 15, 49, 56, 22, 23, 25}
    50 % 7 = 1 so insert in index 1
    21 % 7 = 0 so insert in index 0
    if the index is already filled add additional space and point to it (linkedlist)

    | Index | keys|  | |
    |-----|----|----|----|
    | 0| 21| ---> 49| --->56|
    |1| 50| ----> 15| ---> 22|
    |2| 58|
    |3|17|
    |4|25|

- Performance 
    - m = No. of slots in Hash table 
    - n = No. of keys to be inserted 
    - Load factor  $ \alpha = n/m $
    - Expected chain length = $ \alpha $
    - Expected time to Search = $ O(1 + \alpha) $
    - Expected time to Insert/Delete = $ O(1 + \alpha ) $

- Data structure for Storing chains 
    - Linked List 
        - Search O(l), Delete O(l), Insert O(l) , l = chain length 
        - not cache friendly as nodes are at different locations
        - Uses extra spaces for storing next references or pointers 
    
    - Dynamic Sizes Arrays (list in Python)
        - Same as Linked list 
        - Cache friendly, contigious location 

    - Self Balancing BST (AVL Tree, Red Black Tree)
        - Search, insert, delete : O(log l)
        - Not cache friendly 

- Implementation of Chaining in Python 
    - h = myHash(7) (Bucket size = 7)
    - perform insert operations , search and delete operations 
    - hash in python (list of lists) [ [], [], [], [], []]
    - hash(x) = x % BUCKET
                                     
    | | |
    |--|--|
    |0| [ ] |   
    |1| [ ] |
    |2| [ ] | 
    |3| [ ] |    
    |4| [ ] |
    |5| [ ] |
    |6| [ ] |

    Insert 70,71,9,56,75  

    ||||
    |--|--|--|
    |0| 70| 56   
    |1| 71 |
    |2| 9 | 72 | 
    |3| [ ] |       
    |4| [ ] |
    |5| [ ] |
    |6| [ ] |
    
    [ [70, 56], [71], [9, 72] ]

**Open Addressing**
Another method of handling collision 
- No of slots in hash table $ \geq $ No of keys to be inserted 
- cache friendly 
- Other ways of implementing open Addressing:- linear probing, quadratic probing and double hashing 
- Linear probing example:
    hash(key) = key % 7 => index from 0 to 6 i.e 7 

    |||
    |---|--|
    |0|49|
    |1|50|
    |2|51|
    |3|16|
    |4|56|
    |5|15|
    |6|19|

- Linearlly search for next empty search when there is a collision  
- How to handle deletions in open addressing ? 
    - insert(50), insert(51), insert(15), search(15), delete(15), search(15)
    - Search operation : compute hash function , go to that index and compare , if we find --> done , otherwise we linerally search.
        - Stop when one of the conditions arises 
            1. Empty slot
            2. Key found 
            3. Traversed through whole list 
    - Delete operation : problem with simply making slot empty when we delete key 
        - when we find the slot that's empty we mark it "deleted" and move on to next slot 

- Clustering ( A problem with linear probing)
    - All operations will become costlier at the clusters goes bigger: K --> k+1
- How to handle clustering problem with linear probing ?

    hash(key, i) = (h(key) + i) % 7 

    1. Quadratic Probing

        hash(key, i) = $ (h (key) + i ^2) \% \quad m $
        
        - Secondary cluster
        - might have it doesn't find empty slot even though there are some as we are probing quadraticly 
        - load factor $ \alpha \le 0.5 $ 
        - hash function is a prime number 
    2. Double hashing 
        hash(key, i) = $ (h, (key) + i * h2(key)) \%  m $ 