def lenoflstring(self,s):
    maxlength = 0
    sublength = 0
    lettersUsed = set([])
    start = 0
    for i in range(len(s)):
        if not (s[i] in lettersUsed):
            lettersUsed.add(s[i])
            if i == len(s) - 1:
                maxlength = max(maxlength, i + 1 - start)
        else:
            maxlength = max(maxlength, i - start)
            lettersUsed.remove(s[start])
            start += 1
            while (start <= i) and (s[i] in lettersUsed):
                lettersUsed.remove(s[start])
                start += 1
            lettersUsed.add(s[i])
    return maxlength


lenoflstring("ABCDDEFGHIJKLMM12345677TUVWXYZZ")