def quickSort(arr, low, high):
    if low<high:
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        pi=i+1
        
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr = [10, 7, 8, 9, 1, 5]

quickSort(arr, 0, len(arr) - 1)

print(arr)