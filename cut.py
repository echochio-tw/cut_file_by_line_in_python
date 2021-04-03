with open("2021-04-04-0000-2330_gpkw.bass.log.csv",encoding="utf-8") as myfile:
    Nlines=myfile.readlines()[191424:200850] # from line 191425 to 200851
outF = open("myOutFile.txt", "w") # out to file myOutFile.csv
for line in Nlines:
    outF.write(line)
outF.close()
