# INFINITE Hotel 
from collections import Counter

def captian_room(room_numbers):
    for i in room_numbers:
        if room_numbers.count(i) == 1:
            print(i)
        

# optimized version
def captian_room_opt(room_numbers):
    result = Counter(room_numbers)
    for key, count in result.iteritems():
        if count == 1:
            print(key)

def main():
    size_of_group = int(input('Enter Size of the group: '))
    room_numbers = list(map(int, input().split()))

    captian_room(room_numbers)

if __name__ == '__main__':
    main()