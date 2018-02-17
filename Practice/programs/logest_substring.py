def scantillrepeat(line):
    found = ''
    for char in line:
        if not char in found:
            found = found + char
        else:
            break
    return found


def findlongest(f):
    for line in f:
        longestfound = ''
        longestfoundlen = 0
        for k in range(len(line)):
            candidate = scantillrepeat(line[k:])
            if len(candidate) > longestfoundlen:
                longestfound = candidate
                longestfoundlen = len(candidate)
                print len(candidate)
                print longestfound
    print longestfound

st = ['ABCDDEFGHIJKLMM12345677TUVWXYZZ']
findlongest(st)
