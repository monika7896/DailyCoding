
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def find_max(v):
            return max(v)

        def calculate_total_hours(v, hourly):
            totalH = 0
            print("v",v)
            for bananas in v:
                totalH += (bananas + hourly - 1) // hourly  # Equivalent to ceil(bananas / hourly)
                # print(totalH,"ansss")
            return totalH

        def minimum_rate_to_eat_bananas(v, h):
            low, high = 1, find_max(v)
            # print("vvvv",v)
            while low <= high:
                mid = (low + high) // 2
                print("mid",mid)
                totalH = calculate_total_hours(v, mid)
                if totalH <= h:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        return minimum_rate_to_eat_bananas(piles, h)

# Example usage
piles = [3, 6, 7, 11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))  # Output: 4
