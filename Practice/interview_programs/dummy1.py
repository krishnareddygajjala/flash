string = "venkata krishna reddy"
dup = []
for i in string:
    if i < len(string) - 1:
        i +=1
        if string(i) == string(i + 1):
            dup.append(i)
            print i
print dup



def find_repeater(string):
    my_list = []
    my_list.append(string[0])

    for i in range (1, len(string)):

        if string[i] in my_list:
            print 'repetition found'
            return (string[i])
        else:
            my_list.append(string[i])
            
    print my_list

print find_repeater(string) 