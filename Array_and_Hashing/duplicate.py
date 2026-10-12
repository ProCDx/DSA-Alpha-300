class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    sol = Solution()
    print(sol.containsDuplicate(nums))


if __name__ == "__main__":
    main()