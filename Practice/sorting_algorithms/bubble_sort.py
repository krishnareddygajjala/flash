
def Bubble_Sort(lst):
    print lst
    sort = True
    while sort:
        sort = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                sort = True
    return lst


seq = [2,1,3,12,4,6,7,11,8,10,9]
print Bubble_Sort(seq)
                
