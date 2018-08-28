def findLongest1(s):
    maxlen = 0
    longest = ""
    for i in range(0,len(s)):
        subs = s[i:]
        print subs
        chars = set()
        print chars
        for j,c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            # add 1 when end of string is reached (no break)
            # handles the case where the longest string is at the end
            j+=1
        if j>maxlen:
            maxlen=j
            longest=s[i:i+j]
    return longest

print(findLongest1("experience"))