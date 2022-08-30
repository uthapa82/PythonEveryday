from random import shuffle

# tuples unpacking
def tuple_list():
    lst_ex = [('Apple', 'Steve Jobs'), ('Google', 'Larry Sergey'), ('Amazon', 'Jeff Bezos')]
    for item in lst_ex:
        print(item)
    
    for company, founder in lst_ex:
        print(company)

# Three Cup Monte
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: " )
    
    return int(guess)

def guess_game(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct !!!")
    else:
        print("Wrong guess!!")
        print(mylist)

def main():
    tuple_list()
    example = [' ', 'O', ' ']
    mixed_list = shuffle_list(example)
    user_guess = player_guess()
    guess_game(mixed_list, user_guess)

if __name__ == "__main__":
    main()