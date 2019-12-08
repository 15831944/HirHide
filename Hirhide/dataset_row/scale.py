rowdata=open("YeastNet_row.txt","r")
output=open("YeastNet.txt","w")
for line in rowdata:
    line = line.strip().split()
    num=float(line[2])/5
    new_line=line[:2]
    new_line.append(str(num))
    for item in new_line:
        output.write(item+"\t")
    output.write("\n")
