infile = open("input.txt" , "r")
outfile = open("longestword.txt" , "w")

szavak = [y for x in infile.readlines() for y in x.split()]
hossz = len(szavak[0])

for i in szavak:
    if(len(i) > hossz):
        hossz = len(i)

for i in szavak:
    if(len(i) == hossz):
        print(i, len(i) , file=outfile)

infile.close()
outfile.close()
