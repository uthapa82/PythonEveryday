
# P1.prints put words that start with 's'
import numbers


def word_with_s():
    string_1 = "Print only the words that start with s in this sentence"
    words = string_1.split()
    for word in words:
        if word[0] == 's':
            print(word)

# P2.even number from 0 to 10 
# create a list of all numbers between 1 and 50 divisible by 3
def list_example():
    list_1 = [value for value in range(1, 10) if value%2 == 0]
    print("List ofeven numebr \n", list_1)
    list_2 = [x for x in range(1, 50) if x%3 == 0]
    print("List of number divisible by 3 between 1 and 50\n", list_2)

# P3.length of word even or odd 
def len_of_str():
    len_string = "Print every word in the sentence that has an even number of letters"
    new_lst = len_string.split()
    for i in range(len(new_lst)):
        if(len(new_lst[i])% 2 == 0):
            print(new_lst[i] + " is even!")
        
# p3 soluton
def len_solution():
    len_string = "Print every word in the sentence that has an even number of letters"
    print("\nGiven Solution: ")
    for word in len_string.split():
        if len(word) % 2 == 0:
            print(word + " is even !")

# P4fizzbuzz for nultiple of 3 and 5 
def fizz_buzz():
    print("\n fizzbuzz program: ")
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        if num % 5 == 0:
            result.append("Buzz")
        elif num % 3 == 0:
            result.append("Fizz")
        else:
            result.append(num)
    
    return result

# P5. list of first letter of every word in string 
def list_of_str():
    print("\n Program Number 5: ")
    str_1 = 'Create a list of the first letters of every word in this string'
    new_lst = [word[0] for word in str_1.split()]
    print(new_lst)

def main():
    word_with_s()
    list_example()
    len_of_str()
    len_solution()
    print(fizz_buzz())
    list_of_str()

if __name__ == "__main__":
    main()