class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        counts={}           # fruit type count INSIDE the window
        left,result=0,0

        for right in range(len(fruits)):
            f=fruits[right]
            counts[f]=counts.get(f,0)+1

            while len(counts)>2: #  hasp map used to assign key value pairs ,counting frequency of each fruit type
                g=fruits[left]
                counts[g]-=1           
                if counts[g]==0:
                    del counts[g]         #del if no value left
                left+=1
            length=right-left+1
            if length>result:
                result=length
        return result
    
    
    
    #time complexity-o(n) and space is o(1)
    
    
    
            
