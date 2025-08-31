def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

arr1= [4, 34, 2, 12, 22, -9, 90]
arr2 = bubble_sort(arr1)
print("Sorted array:", arr2)
