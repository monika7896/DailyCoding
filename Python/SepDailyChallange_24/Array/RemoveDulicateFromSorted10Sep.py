# remove duplicate in-place array , if array is already sorted

arr =[1,2,2,3,3,4,7]

class Solution:
    def remove_duplicate(self , arr):       i=0
       
       for j in range(len(arr)):
           if arr[i]!= arr[j]:
               print(arr[i] , arr[j])
               arr[i+1]= arr[j]
               i=i+1
       return i+1
        
obj = Solution()
resp=obj.remove_duplicate(arr)
print(resp)
