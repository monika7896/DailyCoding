## Example 1 for "The strings are anagrams."

# Declare Inputs
inp1 = "listen"
inp2 = "silent"

# Sort Elements
x = [inp1[i] for i in range(0, len(inp1))]
print(x)
x.sort()
y = [inp2[i] for i in range(0, len(inp2))]
y.sort()

# the sorted strings are checked
if x == y:
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
