'''
Implementation of various search algorithms 
'''
from typing import List
from random import randint

# TODO: Alternate implementation using caching mechanism if needed
''''
import os
import pickle
from typing import List
from random import randint

# Cache file paths
CACHE_FILE_BASIC = "cached_basic_names.pkl"
CACHE_FILE_SORTED = "cached_sorted_names.pkl"

def load_names(path: str, cache_file: str) -> List[str]:
    """Return a list of names, either from cache or from the file."""
    # Check if cached data exists
    if os.path.exists(cache_file):
        print(f"Loading names from cache `{cache_file}`...", end="", flush=True)
        with open(cache_file, "rb") as f:
            names = pickle.load(f)
            print("OK")
            return names

    # If no cache, load from the file and cache it
    print(f"Loading names from path `{path}`...", end="", flush=True)
    with open(path, encoding='utf8') as text_file:
        names = text_file.read().splitlines()
        # Cache the data
        with open(cache_file, "wb") as f:
            pickle.dump(names, f)
        print("OK")
        return names

# Load names (either from cache or from files)
basic_names = load_names("names.txt", CACHE_FILE_BASIC)
sorted_names = load_names("sorted_names.txt", CACHE_FILE_SORTED)
'''

def load_names(path: str) -> List[str]:
    """Return a list of names from the given file."""
    print(f"Loading names from path `{path}`...", end="", flush=True)
    with open(path, encoding='utf8') as text_file:
        names = text_file.read().splitlines()
        print("OK")
        return names
    
basic_names = load_names("names.txt")
sorted_names = load_names("sorted_names.txt")
  
#random search, naive implementation 
def random_search(items, search_val):
    while True:
        rand_index = randint(0, len(items) - 1)
        rand_element = items[rand_index]

        if rand_element == search_val:
            return rand_index

def linear_search(items, search_val):
    # time complexity O(n)
    # the built in functon 'in' is implemented in C so it's much faster 
    # enumerate eg. [10, 20, 30] -> (0,10) , (1, 20), (2, 30)
    for indx, val in enumerate(items):
        if val == search_val:
            return indx
    return None # or -1, etc..

def binary_search(items, search_val):
    # number of comparisions are shorter than random and linear 
    # better performance/speed than other searching algorithms worst case O(logn)
    start = 0 
    end = len(items) - 1

    while start <= end:
        mid = start + ((start + end) // 2)
        mid_val = items[mid]

        if mid_val == search_val:
            return mid 
        elif mid_val < search_val:
            start = mid + 1
        else:
            end = mid -1

    return None # value not found


def main():
    test_list = [3, 4, 5, 6]
    print(linear_search(sorted_names, "Fred Astaire"))

if __name__ == "__main__":
    main()  