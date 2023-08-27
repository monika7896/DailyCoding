# Python program to add two binary numbers.
# with o(1) and O(1) time complexity
# Driver code
if __name__ == "__main__":
    # Declaring the variables
    a = "1101"
    b = "100"

    # Calculating binary sum by using bin() and int()
    binary_sum = lambda a, b: bin(int(a, 2) + int(b, 2))
    print(int(a, 2), int(b, 2))
    # calling binary_sum lambda function
    print(binary_sum(a, b)[2:])

    # This code is contributed by AnkThon
