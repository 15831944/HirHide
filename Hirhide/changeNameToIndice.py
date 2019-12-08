#将每个数据集的protein id 转换为数字，并将对应关系储存起来
#graphfiles=["biogrid_yeast_physical_unweighted","collins2007","gavin2006_socioaffinities_rescaled","krogan2006_core"]
graphfiles=["YeastNet"]
for graphfile in graphfiles:
    rowdata=open("dataset_row/"+graphfile+".txt","r")
    truth= open("dataset/"+"mips_3_100.txt","r")
    indice=open("dataset/"+graphfile+"/"+graphfile+".txt","w")
    correspond=open("dataset/"+graphfile+"/correspond.txt","w")
    #cyc2008
    truth_list=set()
    for line in truth:
        l_line = line.strip().split()
        for item in l_line:
            truth_list.add(item)
    namenum={}
    i=0
    for line in rowdata:
        l_line = line.strip().split()
        if l_line[0] in truth_list and l_line[1] in truth_list:
            if l_line[0] not in namenum:
                namenum[l_line[0]]=i
                i+=1
            if l_line[1] not in namenum:
                namenum[l_line[1]]=i
                i+=1
            if len(l_line) == 3:
                indice.write(str(namenum[l_line[0]])+"\t"+str(namenum[l_line[1]])+"\t"+l_line[2]+"\n")
            if len(l_line) == 2:
                indice.write(str(namenum[l_line[0]]) + "\t" + str(namenum[l_line[1]])+"\t"+ "1"+"\n")


    for item in namenum:
        correspond.write(str(namenum[item])+'\t'+item+'\n')
    correspond.close()
    indice.close()
    rowdata.close()