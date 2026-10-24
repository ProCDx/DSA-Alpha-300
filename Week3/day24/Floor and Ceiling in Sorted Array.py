class Solution:
    def getFloorAndCeil(self, x, arr):
        left, right = 0, len(arr) - 1
        floor, ceil = -1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                return [x, x]
            elif arr[mid] < x:
                floor = arr[mid]    # could be the floor, try bigger
                left = mid + 1
            else:
                ceil = arr[mid]     # could be the ceil, try smaller
                right = mid - 1
        return [floor, ceil]