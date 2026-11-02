class Solution:
    def frequencySort(self,s):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        pairs=[]
        for ch in freq:
            pairs.append((ch,freq[ch]))

        n=len(pairs)
        for i in range(n):
            max_index=i
            for j in range(i+1,n):
                if pairs[j][1]>pairs[max_index][1]:
                    max_index=j
            pairs[i],pairs[max_index]=pairs[max_index],pairs[i]
        result=""
        for ch,count in pairs:
            result+=ch*count
        return result