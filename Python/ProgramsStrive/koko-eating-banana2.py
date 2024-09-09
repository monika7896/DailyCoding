
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        total = sum(piles)
        print(total,"T")
        start = math.ceil(total / h)
        print(start,"strt")
        end = res = max(piles)
        print(end,"end")
        count = 0
        for pile in piles:
            v = math.ceil(pile / start)
            print(v,"vvv")
            count += v
        if h >= count:
            return start
        count = 0
        while start < end:
            mid = (start + end) // 2
            c = 0
            for pile in piles:
                v = ceil(pile / mid)
         
                c += v
            if c > h:
                start = mid + 1
            else:
                res = min(res, mid)
                end = mid
        print(res)
        return res
piles = [3, 6, 7, 11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))
  # Output: 4
