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

def string_formating():
    string1 = "{} {} {}".format("Geeks", "For", "Geeks")
    print("Print String in default order: ")
    print(string1)
    
    # positional formatting 
    string2 = "{1} {0} {2}".format("Geeks", "For", "Life")
    print("\nPrint String in Positional order: ")
    print(string2)
    
    # keyword formatting 
    string3 = '{l} {f} {g}'.format(g="Geeks", f="For", l="life")
    print("\nPrint String in order of Keywords: ")
    print(string3)
    
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
    print("String formatting: ")
    string_formating()