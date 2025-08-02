# Example 1: rotete left by 1
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 2,3,4,5,1

class Sol:
    def left_rotate(self, arr: list) -> int:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return 1  # 
        first = arr.pop(0) 
        arr.append(first)   

        return arr

     

arr = [1,2,3,4,5]
obj = Sol()
print(obj.left_rotate(arr))
