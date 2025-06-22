def second_large(arr):
    if len(arr) < 2:
        return None  

    firstMax = secondMax = float('-inf')
    
    for num in arr:
        if num > firstMax:
            secondMax = firstMax
            firstMax = num
        elif firstMax > num > secondMax:
            secondMax = num
    
    return secondMax if secondMax != float('-inf') else None
    
    
arr = [-1,-2,-3,-9,-4]
print(second_large(arr))  
