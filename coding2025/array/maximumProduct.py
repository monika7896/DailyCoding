
# Maximum product of a triplet (subsequence of size 3) in array

def maxProduct(arr):
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
    maxProduct = firstMax * secondMax * thirdMax

    return maxProduct


arr = [10, 3, 5, 6, 20]
print(maxProduct(arr)) 

