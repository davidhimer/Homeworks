import re
infile = open("test.txt" , "r")
outfile = open("Listoflongestwords.txt" , "w")

szavak = re.split(" " , infile)
hossz = len(szavak[0])

for i in szavak:
    if(len(i) > hossz):
        hossz = len(i)

for i in szavak:
    if(len(i) == hossz):
        f.write(i , len(i))

infile.close()
outfile.close()
