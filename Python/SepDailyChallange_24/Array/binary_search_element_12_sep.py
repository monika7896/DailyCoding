class Solution:
    def searchInSorted(self, arr, N, K):
        low, high = 0, N - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == K:
                return 1 
            elif arr[mid] < K:
                low = mid + 1 
                
            else:
                high = mid - 1 
        
        return -1 

# Example usage:
arr = [1, 2, 3, 4, 6]
N = 5
K = 6
obj = Solution()
resp = obj.searchInSorted(arr, N, K)
print(resp)  
