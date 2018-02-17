
lst = []
s ="ABCDDEFGHIJKLMM12345677TUVWXYZZ"
def unique(s):
    i, j = 0, 0
    I, J = 0, 0
    H = set([])
    while j < len(s):
        if s[j] in H:
            H.remove(s[i])
            i += 1
        else:
            H.add(s[j])
            j += 1
        if J - I < j - i:
            I, J = i, j
    return s[I:J]
print unique('ABCDDEFGHIJKLMM12345677TUVWXYZZ')






