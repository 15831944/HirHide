#处理CYC2008原始数据
truth_row = open("CYC2008.txt", "r")
truth = open("truth.txt", "w")
complex_name = open("complex_name.txt", "w")
all=[]
for line in truth_row:
    line=line.strip().split("\t")
    line2=[]
    line2.append(line[0])
    line2.append(line[2])
    all.append(line2)
dic={}
for item in all:
    if item[1] not in dic:
        dic[item[1]]=[]
        dic[item[1]].append(item[0])
    else:
        dic[item[1]].append(item[0])
for key in dic:
    if len(dic[key])>2:
        for node in dic[key]:
            truth.write(node+"\t")
        truth.write("\n")
        complex_name.write(key + "\n")









