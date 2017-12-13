str1 = "Hello"                # A new string using double quotes
str2 = 'Hello'                # Single quotes do the same
str3 = "Hello\tworld\n"       # One with a tab and a newline
str4 = str1 + " world"        # Concatenation
str5 = str1 + str(4)          # Concatenation with a number
str6 = str1[2]                # 3rd character
str6a = str1[-1]              # Last character
#str1[0] = "M"                # No way; strings are immutable
for char in str1: print char  # For each character
str7 = str1[1:]               # Without the 1st character
str8 = str1[:-1]              # Without the last character
str9 = str1[1:4]              # Substring: 2nd to 4th character
str10 = str1 * 3              # Repetition
str11 = str1.lower()          # Lowercase
str12 = str1.upper()          # Uppercase
str13 = str1.rstrip()         # Strip right (trailing) whitespace
str14 = str1.replace('l','h') # Replacement
list15 = str1.split('l')      # Splitting
if str1 == str2: print "Equ"  # Equality test
if "el" in str1: print "In"   # Substring test
length = len(str1)            # Length
pos1 = str1.find('llo')       # Index of substring or -1
pos2 = str1.rfind('l')        # Index of substring, from the right
count = str1.count('l')       # Number of occurrences of a substring

print str1, str2, str3, str4, str5, str6, str7, str8, str9, str10 
print str11, str12, str13, str14, list15
print length, pos1, pos2, count



s = 'Hello, wOrLD'
print s              # 'Hello, wOrLD'
print s.title()      # 'Hello, World'
print s.swapcase()   # 'hELLO, WoRld'
print s.upper()      # 'HELLO, WORLD'
print s.lower()      # 'hello, world'
print s.capitalize() # 'Hello, world'