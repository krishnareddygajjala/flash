f = open("C:\\Users\\Ram\\Desktop\\text123.txt",'w')
f.write("first line \n ")
f.write("second line \n")
lines_of_text = ["a line of text \n", "another line of text \n", "a third line \n"]
f.writelines(lines_of_text)

f.close()