# Remove Duplicates in-place from Sorted Array
# Input: arr[1,1,2,2,2,3,3]
# Output: arr[1,2,3,_,_,_,_]

class Sol:
    def remove_duplicates(self, arr: list) -> list:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return True


        for i in range(0, len(arr)):
            if arr[i] == arr[i + 1]:
               temp =  arr[i+1]
               arr[i+1]=


arr=[1,1,2,2,2,3,3]
obj = Sol()
print(obj.remove_duplicates(arr)) 

# inplace remove and fill with - method 2


class Sol:
    def remove_duplicates(self, arr: list) -> int:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return 1  # Only one element, already unique

        i = 1
        for j in range(1, len(arr)):
            if arr[j] != arr[i - 1]:  # compare to last unique element
                arr[i] = arr[j]
                i += 1

        for k in range(i, len(arr)):
            arr[k] = '_'

        return i  # Return length of unique part


arr = [1, 1, 2, 2, 2, 3, 3]
obj = Sol()
new_len = obj.remove_duplicates(arr)
print("New length:", new_len)
print("Modified array:", arr)

# without fill _ return 




