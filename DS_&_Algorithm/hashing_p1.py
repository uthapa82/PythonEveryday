class MyHash:
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