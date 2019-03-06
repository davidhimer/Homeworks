import re

f = open("test.txt", "r")
str = f.read()
tomb = [int(s) for s in re.findall(r'-?\d+\.?\d*',str)]
a = 0
for i in range(len(tomb)):
    a += tomb[i]
print(a)
