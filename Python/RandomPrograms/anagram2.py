# Python3 program for the above approach
from collections import Counter


# function to check if two strings are
# anagram or not
def check(s1, s2):
    # implementing counter function
    if Counter(s1) == Counter(s2):
        print("The strings are anagrams.")
        print(Counter(s1))
        # Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})

    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)
