# Example 1:
# Input: arr[]= 1 2 3 4 5, num = 3
# Output: 2
# Explanation: 3 is present in the 2nd index

# Example 2:
# Input: arr[]= 5 4 3 2 1, num = 5
# Output: 0
# Explanation: 5 is present in the 0th index


class Sol:
      def search_element(self, arr: list , num:int) -> int:
        if not arr:
            raise ValueError("Input array cannot be empty.")
        for i in range (len(arr)):
            if arr[i] == k:
                return i
                
       
        return -1
     

arr = [1 ,2 ,3 ,4 ,1 ,0 ,0 ,0,2]
num=5
obj = Sol()
print(obj.search_element(arr,num))
