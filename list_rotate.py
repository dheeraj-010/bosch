def rotate_list(list1, n):
    return list1[-n:] + list1[:-n]

list1 = [1,2,3,4,5,6]
n=2

rotated = rotate_list(list1, n)
print("Rotated list:", rotated)
