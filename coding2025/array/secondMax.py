
def second_large(arr):
    firstMax = float('inf')
    seondMax = float('inf')
    for i in range (len(arr)-1):
        if arr[i] > firstMax:
            seondMax=arr[i]
        else:
            firstMax = arr[i]
           
    return seondMax

arr = [12, 35, 1, 10, 34, 1]
print(second_large(arr))

