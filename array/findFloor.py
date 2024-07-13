
class Solution:
    def findFloor(self, A, N, X):
        l = 0
        r = N - 1
        ans = -1  # Initialize ans to -1 for the case where all elements are greater than X
        
        while l <= r:
            mid = (l + r) // 2
            
            if A[mid] <= X:
                ans = mid  # Update ans to current mid as it is a potential candidate for floor
                l = mid + 1  # Move to the right half to search for a smaller floor value
            else:
                r = mid - 1  # Move to the left half
            
        return ans

# Example usage:
N = 7
X = 5 
A = [1, 2, 8, 10, 11, 12, 19]
obj = Solution()
c = obj.findFloor(A, N, X)
print("c:", c)  # Output should be index 1, value 2
