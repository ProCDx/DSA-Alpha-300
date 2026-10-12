# ================= VALID PALINDROME: REVISION NOTES =================
# PATTERN : Two Pointers (opposite ends)
# TRIGGER : compare a sequence with its reverse, ignoring some characters
# IDEA    : left and right pointers move inward, skipping non-alphanumeric
#           characters, comparing lowercase versions. Any mismatch -> False.
# TIME    : O(n)   (each pointer moves at most n steps in total)
# SPACE   : O(1)   (no cleaned copy of the string is built)
# PITFALLS:
#   1. Skip junk with an inner WHILE, not an if.
#   2. Keep left < right in the inner loops, or the pointers cross or go out of range.
#   3. Return True only after the loop finishes. " " and "" are palindromes.
#   4. Middle element of an odd length is never compared, which is fine.
# RELATED : Valid Palindrome II, Two Sum II, Longest Palindromic Substring
# =====================================================================


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def main():
    s = input("Enter a string: ")
    print(is_palindrome(s))


if __name__ == "__main__":
    main()