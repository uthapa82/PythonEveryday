class NormalHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [ [] for x in range(b) ]

    def insert(self, x):
        i = x % self.BUCKET
        self. table[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        # remove function of list gives error 
        # if the element is not in present in hash table 
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]

# open addressing hash class
class OpenAddressingHash:
    EMPTY = -1
    DELETED = -2
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [self.EMPTY] * capacity
        self.size = 0
    
    '''
    support for non-integer keys 
    def hash(self, key):
        return hash(key) % self.capacity
        
    '''
    def hash(self, key):
        return key % self.capacity
    
    def search(self, key):
        h = self.hash(key)
        t = self.table
        i = h
        # -1 => empty slot -2=> deleted 
        while t[i] != self.EMPTY:
            if t[i] == key:
                return True
            i = (i + 1) % self.capacity
            # when whole the hash table is full --> check in linear probing 
            if i == h:
                return False # can use break
        
        return False

    def insert(self, key):
        
        if self.size == self.capacity:
            return False # Table Full
        
        if self.search(key) == True:
            return False # Duplicate
        
        i = self.hash(key)
        t = self.table 
        while t[i] not in (self.EMPTY, self.DELETED):
            i = (i + 1) % self.capacity
        t[i] = key
        self.size += 1
        return True
        
    def remove(self, key):
        h = self.hash(key)
        t = self.table
        i = h
        while t[i] != self.EMPTY:
            if t[i] == key:
                t[i] = self.DELETED
                return True
            i = (i + 1) % self.capacity
            if i == h:
                return False
        
        return False

'''
How to handle cases when -1 and -2 can be input keys ? 
=> None = empty , 
deletes==> create a dummy node and reference to the dummy node in the deleted slot 
'''