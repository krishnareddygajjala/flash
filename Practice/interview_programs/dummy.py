string = 'krishna'
def reverse(inpu):
    if len(inpu) <= 1:
        return inpu
    return reverse(inpu[1:]) + inpu[0]

print reverse(string)
#reverse(string)