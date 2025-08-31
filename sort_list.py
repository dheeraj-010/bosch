def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

list1=[1,2,5,78,-10,-7,100]
a=sort_list(list1)
for i in a:
    print(i,end=" ")