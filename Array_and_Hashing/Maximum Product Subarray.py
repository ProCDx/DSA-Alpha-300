from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMax, curMin = nums[0], nums[0]
        for num in nums[1:]:
            candidates = (num, curMax * num, curMin * num)
            curMin = min(candidates)
            curMax = max(candidates)
            result = max(result, curMax)
        return result


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if not nums:
        print("Empty input")
        return
    print("Maximum product subarray:", Solution().maxProduct(nums))


if __name__ == "__main__":
    main()