# function to print string in middle of
# bound by 
from cgi import test


def join_middle(bound_by, tag_name):
    first =  int(len(bound_by)/2)
    last = len(bound_by)

    result = bound_by[0 : first] + tag_name + bound_by[first : last]
    
    return result
    
def main():
    bound_by = input("Please enter bound by: ")
    tag_name = input("Please enter tag name: ")
    
    print(join_middle(bound_by, tag_name))

if __name__ == "__main__":
    main()