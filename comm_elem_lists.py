list1=[1,7,4,6,3,35,2,60]
list2=[7,45,89,60,57,7,35,90]
list3=[]
for item in list1:
    if item in list2 and item not in list3:
        list3.append(item)

print(list3)  
