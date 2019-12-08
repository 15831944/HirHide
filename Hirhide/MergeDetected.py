#将detected中不同layer里面的社团重合比例较大的进行合并
graphfiles=["biogrid_yeast_physical_unweighted","collins2007","gavin2006_socioaffinities_rescaled","krogan2006_core","krogan2006_extended"]
for graphfile in graphfiles:
    rowdata=open("dataset/"+graphfile+"/detected_no_merge.txt","r")
    detected=open("dataset/"+graphfile+"/HICODE.txt","w")
    communities=[]
    for line in rowdata:
        l_line = line.strip().split()
        communities.append(l_line)
    end=len(communities)
    k=0
    for i in range(end):
        if i<end-k:
            union=set(communities[i])
            for j in range(i+1,end):
                if j < end - k:
                    union_val=union | set(communities[j])
                    minus_val=union & set(communities[j])
                    if len(minus_val)/len(union_val)>0.8:
                        union=union_val
                        del communities[j]
                        k+=1
                        print(k)
            #print(i)
            for item in union:
                detected.write(item+'\t')
            detected.write('\n')
