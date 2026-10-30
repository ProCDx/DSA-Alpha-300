class Solution:
    def getSecondLargest(self, arr):
        
        largest=float('-inf')
        second=float('-inf')
        
        for num in arr:
            if num>largest:
                second=largest
                largest=num
            elif num>second and num!=largest:
                second=num
        if second==float('-inf'):
            return -1
        else:
            return second