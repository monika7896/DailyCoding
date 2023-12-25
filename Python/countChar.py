## Example 1 for "The strings are anagrams."

# Declare Inputs
inp1 = "hello   World"

# Sort Elements
my_list = [inp1[i] for i in range(0, len(inp1))]
print(my_list)

# Initialize an empty dictionary to store counts
count_dict = {}

# Iterate through the list
for element in my_list:
    if element != " ":  # Ignore spaces
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1

print(count_dict)
