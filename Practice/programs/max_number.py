lst = [1,36,89,56,98,101,26,123,23,2,65]
max_number = 1
for val in lst:
    if max_number < val:
        max_number = val
        
print max_number
print max(lst)
    