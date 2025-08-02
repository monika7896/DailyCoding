# Check if an Array is Sorted

class Sol:
    def find_sorted_arr(self, arr: list) -> bool:
        if not arr:
            raise ValueError("Input array cannot be empty.")

        if len(arr) == 1:
            return True

        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


# arr = [2, 5, 1, 3, 0]
arr=[1,2,3,4,5,6,7]
obj = Sol()
print(obj.find_sorted_arr(arr)) 