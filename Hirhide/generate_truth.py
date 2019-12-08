#生成各个数据集对于truth的id
graphfiles=["biogrid_yeast_physical_unweighted","YeastNet","krogan2006_core"]
#types=["_cyc/","_mips/"]
types=["_cyc/"]
for onegraph in graphfiles:
    for type in types:
        base="dataset"+type
        truth_row = open(base+"truth.txt", "r")
        graph=open(base+onegraph+"/correspond.txt","r")
        truth=open(base+onegraph+"/truth.txt","w")
        dic_co={}
        for line in graph:
            line=line.strip().split()
            dic_co[line[1]]=line[0]
        for line in truth_row:
            index_line=[]
            line=line.strip().split()
            for item1 in line:
                if item1 in dic_co:
                    index_line.append(dic_co[item1])
            if len(index_line)>2:
                #print(index_line)
                for item2 in index_line:
                    truth.write(item2+"\t")
                truth.write("\n")




