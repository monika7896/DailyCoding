class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid = (l+r) // 2
            print("mid",mid)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r= mid-1
            else :
                l=mid+1
        return -1
