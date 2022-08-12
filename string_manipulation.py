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
    print("String formatting: ")
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
    
    # isalpha(), isalnum(), isspace()
    str = "geeksforgeeks"
    str1 = "123"
    if(str.isalpha()):
        print("All characters are alphabets in str")
    else:
        print("All characters are not alphabets in str")
    if(str1.isalnum()):
        print("All characters are number in str1")
    else:
        print("All characters are not numbers in str1")
    if(str1.isspace()):
        print("All characters are spaces in str1")
    else:
        print("All characters are not spaces in str1")
    
    # using join() to join sequence str1 with str 
    str3 = "_"
    str4 = ("geeks", "for", "geeks") #"Geeks for Geeks" #
    print("\nThe string after joining is: ", end="")
    print(str3.join(str4))
            
# integers such as binary, hex etc and floats can be rounded or 
# displayed in the exponent form with the use of format
def math_format():
    math1 = '{0:b}'.format(16)
    print("\nBinary representation of 16 is ")
    print(math1)
    
    # format floats 
    math2 = "{0:e}".format(165.6458)
    print("\nExponent representation of 165.6458 is ")
    print(math2)
    
    # rounding off integers 
    math3 = '{0:.2f}'.format(1/6)
    print("\none-sith is: ")
    print(math3)
    
def main():
    gfg = 'geeksforgeeks'
    print(gfg[::-1])
    
    # using join and reversed function
    gfg = "".join(reversed(gfg))
    print(gfg)
    
    string_formating()
    
    math_format()
    
    
if __name__ == '__main__':
    print(reversed_string('geeks'))
    reversed_sol2('hey')
    main()
    
    