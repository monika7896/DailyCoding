class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l=0
        r=len(nums)-1
        
        while l<=r:
            if nums[l]+nums[r] == target:
                return [l,r]
            elif nums[l]+nums[r] < target:
                l=l+1
                
            elif nums[l]+nums[r] > target:
                r=r-1
                
        
        
nums = [2,3,4,5,6,7]
target=9

obj = Solution()
c=obj.twoSum(nums ,target)
print(c)


        
        
        
        
