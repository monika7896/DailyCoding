class Solution:
    def sumTarget(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        resp = []

        for i, n in enumerate(nums):
            diff = target - n
            print("diff", diff, i, n)
            if diff in prevMap:
                print("prev", prevMap)
                print("resp", [prevMap[diff], i])
                resp += [(prevMap[diff], i)]
            prevMap[n] = i

        return resp


solution = Solution()
result = solution.sumTarget([1, 2, 36, 7, 4, 5], 9)
print(result)
