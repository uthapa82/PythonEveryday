# tuples 

def tuples_eg1(lst):
    tuple1 = ()
    print("\n Initial empty tuple: ")
    print(tuple1)
    tuple1 = ("VA", "NJ", "NY", "OK")
    print(tuple1)
    
    print("\n Creating Tuples with list: ")
    print(tuple(lst))

# tuples are immutable and are accessed via unpacking or indexing  
def tuples_eg2():
    tuple2 = tuple("Hello Virginia")
    print("\nfirst element of tuple: ", tuple2[0])
    
    # tuple unpacking 
    tuple3 = ("hello", "VA")
    a, b = tuple3
    print("\nValues after unpacking: ")
    print(a)
    print(b)
    
    
def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    tuples_eg1(lst1)
    tuples_eg2()

if __name__ == "__main__":
    main()