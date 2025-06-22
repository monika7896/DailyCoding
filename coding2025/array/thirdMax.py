def third_largest(arr):
    if len(set(arr)) < 3:
        return None  
    
    firstMax = secondMax = thirdMax = float('-inf')

    for num in arr:
        if num > firstMax:
            thirdMax = secondMax
            secondMax = firstMax
            firstMax = num
        elif firstMax > num > secondMax:
            thirdMax = secondMax
            secondMax = num
        elif secondMax > num > thirdMax:
            thirdMax = num

    return thirdMax if thirdMax != float('-inf') else None


arr = [1, 14, 2, 16, 10, 20]
print(third_largest(arr))  # Output: 14
