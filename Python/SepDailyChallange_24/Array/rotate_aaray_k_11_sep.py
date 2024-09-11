// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
// firstly reverse first part like till k and then reverse second part from k to n and finally reverse complete arraya which contains 2 reverse arrays.

class Solution:
    def reverse(self, nums, start, end):
        while start < end :
            nums[start] , nums[end] = nums[end] , nums[start]
            start = start+1
            end = end -1

    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        
        k= k % n
        self.reverse(nums, 0 , n-k-1)
        self.reverse(nums ,n-k  , n-1)
        self.reverse(nums , 0 ,n-1)
        
        return nums
       
