def longest_subarray_sum_k(arr, k):
    first = {0: -1}          # prefix sum -> FIRST index where it appeared
    total = 0
    best = 0

    for i in range(len(arr)):
        total += arr[i]                  #  running prefix sum

        need = total - k                 # what earlier prefix would make a sum-k subarray?
        if need in first:
            length = i - first[need]
            if length > best:
                best = length

        if total not in first:           #  store only the FIRST index
            first[total] = i

    return best



#time complexity-o(n) and space is o(1)