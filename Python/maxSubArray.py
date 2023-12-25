class Solution:
    def maxSum(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            print("curSumeeee", curSum)
            maxSub = max(maxSub, curSum)
            print("maxSubOuter", maxSub)

        return maxSub


solution = Solution()
result = solution.maxSum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)

"""curSumeeee -2
maxSubOuter -2
curSumeeee 1
maxSubOuter 1
curSumeeee -2
maxSubOuter 1
curSumeeee 4
maxSubOuter 4
curSumeeee 3
maxSubOuter 4
curSumeeee 5
maxSubOuter 5
curSumeeee 6
maxSubOuter 6
curSumeeee 1
maxSubOuter 6
curSumeeee 5
maxSubOuter 6"""
