# similar to dynamic sized arrays, declared in other languages(vector in C++ and arrayList in Java )
# complexities for creating lists
# O(1) --> time complexity, O(n)-----> space complexity 

# example of multidimensional list 
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

lst1 = [2, 4, 6, 8]
lst2 = [1,2,3,4,5,6,7,8]
print(union(lst1, lst2))

