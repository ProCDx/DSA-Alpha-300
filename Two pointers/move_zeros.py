# ================= MOVE ZEROES: REVISION NOTES =================
# PATTERN : Two Pointers (same direction: read / write)
# TRIGGER : rearrange an array IN PLACE, keep relative order of some elements
# IDEA    : read scans the array; write marks the next slot for a non-zero.
#           On a non-zero, swap nums[read] with nums[write], then write += 1.
# TIME    : O(n)   (one pass)
# SPACE   : O(1)   (in place, no copy)
# PITFALLS:
#   1. Don't build a new list; the problem demands in-place.
#   2. Don't remove/insert inside the loop; it shifts elements, O(n^2).
#   3. If there are no zeros, read == write and each swap is with itself. Harmless.
#   4. Dry-run [0], [1], [0,0,1], [1,2,3] before submitting.
# RELATED : Remove Duplicates from Sorted Array, Remove Element
# ================================================================


def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            temp = nums[write]
            nums[write] = nums[read]
            nums[read] = temp
            write += 1


def main():
    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    move_zeroes(nums)
    print(nums)


if __name__ == "__main__":
    main()