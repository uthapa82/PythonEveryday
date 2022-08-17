import re 

def number_matcher(str):
    pat = "\d+"
    match = re.findall(pat, str)
    if(match):
        for i in match:
            print(i, end=" ")
    else:
        print(-1, end="\n")
    print("\n")
    
def password_validator(str):
    pat = ('[a-z]+[!@#$%]+[\d+]')
    match = re.search(pat, str)
    if(match):
        print("True")
    else:
        print("False")

def main():
    user_string = input("Enter random password: ")
    number_matcher(user_string)
    password_validator(user_string)
    
if __name__ == "__main__":
    main()