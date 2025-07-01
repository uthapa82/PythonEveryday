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
    def __init__(self, c):
        self.capacity = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, x):
        return x % self.capacity
    
    def search(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        # -1 => empty slot -2=> deleted 
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i + 1) % self.capacity
            # when whole the hash table is full --> check in linear probing 
            if i == h:
                return False
        
        return False

    def insert(self, x):
        
        if self.size == self.cap:
            return False 
        
        if self.search(x) == True:
            return False
        
        i = self.hash(x)
        t = self.table 
        while t[i] not in (-1, -2):
            i = (i + 1) % self.capacity
        t[i] = x
        self.size = self.size + 1
        return True
        
    def remove(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
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