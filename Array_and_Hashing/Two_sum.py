def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i


def main():
    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    target = int(input("Enter target: "))
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
    
# ===================== TWO SUM: REVISION NOTES =====================
# PATTERN : Hash Map / Complement Lookup
# TRIGGER : unsorted array + find a pair + return INDICES
# IDEA    : for each x, look for ONE value: need = target - x.
#           Store seen values in a hash map -> O(1) lookup.
# TIME    : O(n)   (one pass, O(1) average per lookup)
# SPACE   : O(n)   (map can hold up to n elements)
# BRUTE   : check every pair -> O(n^2) time, O(1) space
# PITFALLS:
#   1. Insert AFTER checking, or [3,2,4] t=6 pairs 3 with itself.
#   2. Duplicates are fine: [3,3] t=6 works.
#   3. Store INDEX as the value (problem wants indices).
#   4. Don't sort + two pointers: sorting destroys indices.
# RELATED : Two Sum II (sorted -> two pointers), 3Sum (fix one + two sum)
# ====================================================================
