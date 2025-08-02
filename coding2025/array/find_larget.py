# Find the Largest element in an array

# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array. 

class Sol:
    def find_largest(self , arr:list )-> int:
        if not arr:
            raise ValueError("Input array cannot be empty.")
         
        if len(arr) == 1:
            return arr[0]
            
        maxEle = arr[0]  
        for num in arr:
            if num > maxEle:
                maxEle = num
                
        return maxEle
        
arr=[2,5,1,3,0]
obj =  Sol()
print(obj.find_largest(arr))

