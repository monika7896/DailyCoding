def find_peak(arr):
    def binary_search_peak(arr, low, high):
        mid = low + (high - low) // 2
        
        # Check if mid is a peak element
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return mid
        # If the left neighbor is greater, then the peak must be on the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search_peak(arr, low, mid - 1)
        # Otherwise, the peak must be on the right half
        else:
            return binary_search_peak(arr, mid + 1, high)
    
    return binary_search_peak(arr, 0, len(arr) - 1)

arr = [1, 3, 20, 4, 1, 0]
peak_index = find_peak(arr)
print(peak_index)
