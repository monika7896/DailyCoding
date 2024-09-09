#User function Template for python3


class Solution:
    def findKRotation(self, arr):
        l, h = 0, len(arr) - 1
        index = -1
        ans = float('inf')

        while l <= h:
            # If the subarray is already sorted or only one element left
            if arr[l] <= arr[h]:
                if arr[l] < ans:
                    ans = arr[l]
                    index = l
                break

            m = (l + h) // 2

            # Update ans and index if a smaller element is found
            if arr[m] < ans:
                ans = arr[m]
                index = m

            # Decide which half to continue searching in
            if arr[m] >= arr[l]:
                l = m + 1
            else:
                h = m - 1

        return index

