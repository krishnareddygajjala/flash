def key_fun(o):
    if o % 2 == 0:
        return 0
    else:
        return 1

arr = (4, 5, 7, 2, 1, 5000, 1503, 763, 0, 1)
arr_sorted = sorted(arr, key=key_fun)
print(arr_sorted)