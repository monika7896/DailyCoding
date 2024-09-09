class Solution:
    def duplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


solution = Solution()
result = solution.duplicate([1, 2, 3, 1])
print(result)
