class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left,right=0,0
        total=0
        result=len(nums)+1
        for right in range(len(nums)):#shifting from left to right and sliding when total is equal to or greater than target
            total+=nums[right]
            while total>=target:
                if right-left+1<=result:#without using min() we can check like this
                    result=right-left+1
                total-=nums[left]
                left+=1
        if result == len(nums) + 1:
            return 0
        return result


#time complexity-o(n) and space is o(1)
#Pattern: variable-size sliding window.
#Trigger: contiguous subarray, all positives, and we want the shortest or longest one satisfying a sum condition.
#Why it works: positives mean adding grows the sum and removing shrinks it. With negatives this breaks, which is why
#              Problem 2 needs a different approach.