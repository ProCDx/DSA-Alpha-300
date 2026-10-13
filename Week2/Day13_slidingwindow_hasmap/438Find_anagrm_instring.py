class Solution:
    def findAnagrams(s, p):
        if len(p) > len(s):
            return []

        size = len(p)
        p_count = {}
        window_count = {}

        for i in range(size):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            window_count[s[i]] = window_count.get(s[i], 0) + 1

        result = []
        if window_count == p_count:
            result.append(0)


        left = 0
        for right in range(size, len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1   

            window_count[s[left]] -= 1                                   
            if window_count[s[left]] == 0:
                del window_count[s[left]]                                 
            left += 1

            if window_count == p_count:
                result.append(left)                                       # left = window start

        return result