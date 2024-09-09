arr=[4,5,1,2,7,0]


class Solution:
    def getLargest(self, arr):
        larges = arr[0]
        for i in range(len(arr)):
            if arr[i] >= larges:
                larges = arr[i]
                i = i+1
            
        return larges
        
obj = Solution()
resp = obj.getLargest(arr)
print(resp)
