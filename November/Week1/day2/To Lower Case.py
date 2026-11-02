#Brute Force:
class Solution:
    def toLowerCase(self, s: str) -> str:
        result=''
        for ch in s:
            if "A"<=ch<="Z":
                result+=chr(ord(ch)+32)
            else:
                result+=ch
        return result
#Time complexity:O(n^2),space complexity:O(n)
#Optimal:
class Solution:
    def toLowerCase(self, s: str) -> str:
        result=[]
        for ch in s:
            if "A"<=ch<="Z":
                ch=chr(ord(ch)+32)
            result.append(ch)
        return "".join(result)
#Time complexity:O(n),space complexity:O(n)
    