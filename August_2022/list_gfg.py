# similar to dynamic sized arrays, declared in other languages(vector in C++ and arrayList in Java )
# complexities for creating lists
# O(1) --> time complexity, O(n)-----> space complexity 

# example of multidimensional list 
def general_list():
    list2 = [['Ashburn', 'VA'], ['Lawrence', 'NJ']]
    print(list2[1][0])
    print(list2[1][1])
    
    # complexities of accessing elements in a list :-
    # time complexity: O(1) 
    # space complexity: O(1)  ---> constant time 
    # input
      
    n = input("Enter the elements in  the list: ")
    user_input = n.split()
    # store integers in a list using map 
    # split and strip functions 
    
    print("The list is: ", user_input)
    # list comprehension syntax
    # newList = [expression(element) for element in oldList if condition]
    
    odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
    print(odd_square)

# union of 2 lists 
def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

# intersection 
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def another_approach(lst1, lst2):
    return list(set(lst1) & set(lst2))

# yet another approach using hybrid method,the complexity of
# the program falls to O(n) most efficient way of doing 
def most_efficient_intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3

def main():
    # general_list()
    lst_1 = [2, 4, 6, 8, 10]
    lst_2 = [1, 2, 3, 4]
    print(intersection(lst_1, lst_2))
    print("Intersection using set(): ", another_approach(lst_1, lst_2))
    
    #Python program to illustrate union
    lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
    lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
    lst1.extend(lst2)
    #Maintaining repetition
    print("Maintaining repetition "+str(lst1))
    #Not maintaining repetition and order
    x=list(set(lst1))
    print("Not maintaining repetition "+str(x))


if __name__ == "__main__":
    main()