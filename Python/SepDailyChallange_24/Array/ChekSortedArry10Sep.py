# check If array is soreted

arr =[1,2,2,3,4,5,6,6,7]

class Solution:
    def check_sorted_array(self , arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
        
obj = Solution()
resp=obj.check_sorted_array(arr)
print(resp)
