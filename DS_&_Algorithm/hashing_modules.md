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
