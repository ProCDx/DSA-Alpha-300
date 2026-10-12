# ================= VALID ANAGRAM: REVISION NOTES =================
# PATTERN : Hash Map / Frequency Count
# TRIGGER : compare two strings/arrays by character counts, order ignored
# IDEA    : count chars of s, then consume those counts using t.
#           Any char missing or exhausted -> not an anagram.
# TIME    : O(n)   (two passes, O(1) average per dict operation)
# SPACE   : O(k)   (k = distinct characters, O(1) for lowercase letters)
# PITFALLS:
#   1. CHECK LENGTHS FIRST. s="ab", t="a" wrongly returns True without it.
#   2. Check "count == 0" as well as "not in counts", or extra chars slip through.
#   3. Empty strings: both empty -> True.
# ALTERNATIVES: sorted(s) == sorted(t) is O(n log n); Counter(s) == Counter(t) is O(n).
# RELATED : Group Anagrams, Find All Anagrams in a String
# ==================================================================


def is_anagram(s, t):
    if len(s) != len(t):               # pitfall 1: different length -> impossible
        return False
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
    return True


def main():
    s = input("Enter first string: ")
    t = input("Enter second string: ")
    print(is_anagram(s, t))


if __name__ == "__main__":
    main()