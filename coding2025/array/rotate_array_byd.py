# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position 

class Sol:
    def reverse_array(self, arr, start:int , end:int)-> list:
        
        while start < end:
            arr[start], arr[end] = arr[end] , arr[start]
            start = start+1
            end = end-1

    
    def right_rotate(self, arr: list , d:int) -> int:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return 1 
            
        n = len(arr)
        d = d % n  
           
        self.reverse_array(arr ,0,n-1)    
        self.reverse_array(arr ,0, d-1)  
        self.reverse_array(arr, d, n - 1)

        return arr
     

arr = [1,2,3,4,5,6,7]
d=2
obj = Sol()
print(obj.right_rotate(arr,d))
