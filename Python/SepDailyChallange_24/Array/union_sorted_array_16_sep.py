// get union of array from sorted array

class Solution:
    def findUnion(self, arr1, arr2, n, m):
        i, j = 0, 0
        union_array = []
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not union_array or union_array[-1] != arr1[i]:
                    union_array.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union_array or union_array[-1] != arr2[j]:
                    union_array.append(arr2[j])
                j += 1
            else:  # If both elements are same
                if not union_array or union_array[-1] != arr1[i]:
                    union_array.append(arr1[i])
                i += 1
                j += 1
        
        # Add remaining elements from arr1
        while i < n:
            if union_array[-1] != arr1[i]:
                union_array.append(arr1[i])
            i += 1
        
        # Add remaining elements from arr2
        while j < m:
            if union_array[-1] != arr2[j]:
                union_array.append(arr2[j])
            j += 1
        
        return union_array

# Test
arr1 = [1, 2, 3, 3, 4, 4, 5]
arr2 = [2, 3, 4, 5, 6, 6, 7, 8]
n = len(arr1)
m = len(arr2)

obj = Solution()
resp = obj.findUnion(arr1, arr2, n, m)
print(resp)
