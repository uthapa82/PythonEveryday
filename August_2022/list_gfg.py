# similar to dynamic sized arrays, declared in other languages(vector in C++ and arrayList in Java )
# complexities for creating lists
# O(1) --> time complexity, O(n)-----> space complexity 

# example of multidimensional list 
list = [['Ashburn', 'VA'], ['Lawrence', 'NJ']]
print(list[1][0])
print(list[1][1])

# complexities of accessing elements in a list :-
# time complexity: O(1) 
# space complexity: O(1)  ---> constant time 


# input  
n = input("Enter the elements in  the list: ")
user_input = n.split()
# store integers in a list using map 
# split and strip functions 


print("The list is: ", user_input)