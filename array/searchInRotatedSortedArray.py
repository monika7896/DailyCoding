nums = [4,5,6,7,0,1,2]
target = 0

# Output: 4

#User function Template for python3
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid = (l+r)//2
    
            midVal = nums[mid]
            if midVal == target:
                return mid
            elif nums[l] <= midVal:
                if (nums[l] <=target  and target <= midVal):
                    r=mid-1
                else:
                   l=mid+1
               
            else:
                 if (target >= midVal and target <= nums[r]):
                     l=mid+1
                 else:
                    r=mid-1
        return -1
	            

obj = Solution()
c=obj.search(nums,target)
print("c",c)
