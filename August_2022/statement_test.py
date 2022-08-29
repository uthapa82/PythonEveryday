
# P1.prints put words that start with 's'
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
    pass

# P4fizzbuzz for nultiple of 3 and 5 
def fizz_buzz():
    pass

# P5. list of first letter of every word in string 
def list_0f_str():
    pass

def main():
    word_with_s()
    list_example()

if __name__ == "__main__":
    main()