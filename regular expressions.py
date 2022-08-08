import re
txt="Use of python in Machine Learning"
x=re.search("^Use.*Learning$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")




txt="Use of python in Machine Learning"
x=re.findall("in", txt)
print(x)

txt="Python is one of the most popular languages"
searchObj = re.search("\s",txt)
print("The first white-space character is located ")
