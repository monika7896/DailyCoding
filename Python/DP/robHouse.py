class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            print("temp", temp)
            rob1 = rob2
            print("rob1", rob1)
            rob2 = temp
            print("rob2", rob2)

        return rob2


solution = Solution()
result = solution.rob([1, 2, 3, 5])
print(result)
