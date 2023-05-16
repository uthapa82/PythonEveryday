"""
    integers in pythin can be as big ad the bytes in our machine's memory 
    there's no limit in size as there is 2^31 - 1(c++ int) or 2^63 -1 (c++ long long int)

"""

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    result = pow(a, b) + pow(c, d)

    print(result)

if __name__ == "__main__":
    main()