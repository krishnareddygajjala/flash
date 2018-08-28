def findLongest(inputStr):
    resultSet = []
    substr = []

    for c in inputStr:
        print ("c: ", c)
        if substr == []:
            substr.append([c])
            continue

        print(substr)
        
        for idx, str in enumerate(substr):
            print ("c: ",c," - str: ",str,"\n")
            if c in str:
                resultSet.append(str)
                substr[idx] = []
            else:
                str.append(c)

    print("Result set:")
    print(resultSet)
    return ''.join(max(resultSet, key=len))

print (findLongest("pwwkewambb"))

def findLongest1(s):
    maxlen = 0
    longest = ""
    for i in range(0,len(s)):
        subs = s[i:]
        chars = set()
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

print(findLongest1("pwwkewambb"))