# in python string are arrays of bytes representing Unicode characters 
# python doesn't have character data types 

#reversing a string 
def reversed_string(txt):
    result = ""
    for char in txt:
        result = char + result
    return result

def reversed_sol2(text):
    for i in reversed(text):
        print(i)
        
    
def main():
    gfg = 'geeksforgeeks'
    print(gfg[::-1])
    
    # using join and reversed function
    gfg = "".join(reversed(gfg))
    print(gfg)

if __name__ == '__main__':
    main()
    print(reversed_string('geeks'))
    reversed_sol2('hey')