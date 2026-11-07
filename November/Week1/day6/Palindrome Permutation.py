class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        odd=set()
        
        for ch in s:
            if ch in odd:
                odd.remove(ch)
            else:
                odd.add(ch)
        return len(odd)<=1