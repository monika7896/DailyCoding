class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] == target:
                    return [i , i+1]
        
        
nums = [2,3,4,5,6,7]
target=9

obj = Solution()
c=obj.twoSum(nums ,target)
print(c)


        
        
        
        
