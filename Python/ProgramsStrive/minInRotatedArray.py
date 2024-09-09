class Solution:
    def findMin(self, nums: list[int]) -> int:
        l=0 
        h=len(nums)-1 
        ans=max(nums)
        while l <= h :
            m = (l+h)//2
            if (nums[l]<= nums[m]):
                ans=min(ans,nums[l])
                l=m+1

            else :
                ans=min(ans,nums[m])
                h=m-1
        return ans

nums = [3,1,2]


# Output: 1

obj = Solution()
resp= obj.findMin(nums)
print(resp)
