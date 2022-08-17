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
    
def password_validator():
    pass

def main():
    user_string = input("Enter random password: ")
    number_matcher(user_string)
    
if __name__ == "__main__":
    main()