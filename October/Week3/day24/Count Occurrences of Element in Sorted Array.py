class Solution:
    def countFreq(self, arr, target):

        def find(first):
            left, right = 0, len(arr) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    ans = mid
                    if first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        first = find(True)
        if first == -1:
            return 0
        last = find(False)
        return last - first + 1