# method 1

def move_zeros_end(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] != 0:
            arr[i] , arr[count] = arr[count] ,arr[i]
            count += 1
    return arr
    
arr = [1, 2, 0, 4, 3, 0, 5, 0]    
print(move_zeros_end(arr))


# using class method 2


# Example 1:
# Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
# Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order


class Sol:
      def move_zeros(self, arr: list) -> int:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return arr
        i = 0
        for j in range(len(arr)):
            if arr[j] != 0 :
                arr[j] , arr[i] = arr[i] , arr[j]
                i=i+1
                
       
        return arr
     

arr = [1 ,2 ,3 ,4 ,1 ,0 ,0 ,0,2]
obj = Sol()
print(obj.move_zeros(arr))
