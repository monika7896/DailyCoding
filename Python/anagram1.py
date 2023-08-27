# function to check if two strings are
# anagram or not
def check(s1, s2):
    print(sorted(s1))
    print(sorted(s2))
    # ['e', 'i', 'l', 'n', 's', 't']
    # the sorted strings are checked
    if sorted(s1) == sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)
