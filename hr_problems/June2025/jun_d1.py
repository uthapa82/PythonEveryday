import re

#polynomial solve 
def pol_solve():
    x, k = map(int, input().split())
    polynomial = input()
    result = eval(polynomial.replace('x', str(x)))
    print(result == k)

#group(), groups() and groupdict()
'''
    Input: "abccde"

    Regex matches 'cc', so m.group(1) returns 'c'.

    m.group(1) if m else -1
    If a match is found, return the first repeated character.

    Otherwise, return -1.
    
    def first_repeating_char(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return s[i]
    return -1

    if __name__ == "__main__":
        user_input = input().strip()
        print(first_repeating_char(user_input))
'''
def group_problems():
     
    m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
    print(m.group(1) if m else -1)

def main():
    group_problems()


if __name__ == '__main__':
    main()