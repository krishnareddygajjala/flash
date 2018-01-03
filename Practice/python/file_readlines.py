def read_lines(filename):
    '''
    read the content of a given file
    '''
    fobj = open(filename,"r")
    data = fobj.readlines()
    fobj.close()
    return data

data1 = read_lines("sample.txt")
print data1