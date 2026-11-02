class Solution:
    def inversionCount(self, arr):
        if len(arr) <= 1:                      
            return 0

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        count = 0
        count += self.inversionCount(left)     
        count += self.inversionCount(right)    

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:           
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                count += len(left) - i         
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return count