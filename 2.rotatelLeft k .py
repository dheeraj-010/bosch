def rotateLeft(arr,k):
    while k:
        arr.append(arr.pop(0))
        k-=1
    return arr

n=int(input("Size of array :"))
print("Enter the array: ")
arr1=[]
for i in range(n):
    a=int(input())
    arr1.append(a)
k=int(input("rotate by : "))
a=rotateLeft(arr1,k)
print("The rotated array is :",a)