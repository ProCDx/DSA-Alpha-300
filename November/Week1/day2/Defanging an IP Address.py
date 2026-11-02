#brute force
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=""
        for ch in address:
            if ch ==".":
                result+="[.]"
            else:
                result+=ch
        return result
#Time complexity:O(n^2),space complexity:O(n)
#optimal
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=[]
        for ch in address:
            if ch ==".":
                result.append('[.]')
            else:
                result.append(ch)
        return "".join(result)
#Time complexity:O(n),space complexity:O(n)