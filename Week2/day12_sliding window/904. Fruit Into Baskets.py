def totalFruit(fruits):
    counts = {}                          # fruit type count INSIDE the window
    left = 0
    best = 0

    for right in range(len(fruits)):
        f = fruits[right]
        counts[f] = counts.get(f, 0) + 1     #  expand and add the counts of each fruit

        while len(counts) > 2:              
            g = fruits[left]
            counts[g] -= 1                   #  shrink
            if counts[g] == 0:
                del counts[g]                
            left += 1

        length = right - left + 1           
        if length > best:
            best = length

    return best