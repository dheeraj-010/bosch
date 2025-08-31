def binary_search(arr, target):
    l=0
    h=len(arr)-1

    while l<=h:
        mid=(l+h)//2

        if arr[mid]==target:
            return mid 
        elif arr[mid]<target:
            l=mid +1
        else:
            h=mid-1

arr1=[1,4,6,8,4,12,15,80,100,67,7]
arr2=sorted(arr1)
print("The element is found at position :" ,binary_search(arr2,15))