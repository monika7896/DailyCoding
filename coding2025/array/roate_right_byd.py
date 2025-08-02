# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position 
# method 1
class Sol:
    def right_rotate(self, arr: list , d:int) -> list:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return 1 
            
        n =len(arr)
        d = d % n
        result =  arr[-d:] + arr[:-d] 
        return result

     

arr = [1,2,3,4,5,6,7]
d=2
obj = Sol()
print(obj.right_rotate(arr,d))
