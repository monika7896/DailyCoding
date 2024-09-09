//find secons large element in the array
class Solution:
    def getSecondLarge(self, arr):
        if len(arr) < 2:
            return None 
        
        largest = float('-inf')
        secondLarge = float('-inf')

        for i in range(len(arr)):
            if arr[i] > largest :
                secondLarge = largest
                largest = arr[i]
            elif arr[i] > secondLarge and  arr[i] < largest:
                secondLarge = arr[i]
            
        return secondLarge if secondLarge != float('-inf') else None
   
    
obj = Solution()
resp= obj.getSecondLarge(arr)
print(resp)
