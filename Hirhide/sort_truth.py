graphfiles=["biogrid_yeast_physical_unweighted","YeastNet","krogan2006_core"]
#graphfiles=["YeastNet"]
#types=["_cyc/","_mips/"]
types=["_cyc/"]
for file in graphfiles:
    for type in types:
        base = "dataset" + type
        a=open(base+file+"/truth.txt","r")
        b=open(base+file+"/truth","w")
        list=[]
        sort_list=[]#sort_list[0]为列表在list中的位置，sort_list[1]为列表的长度
        for line in a:
            l_line=line.strip().split()
            list.append(l_line)
        for i in range(len(list)):
            one=[]
            one.append(i)
            one.append(len(list[i]))
            sort_list.append(one)
        sort_list.sort(key=lambda x:x[1],reverse=True)
        #sort_list.sort(key=sort_list[1])
        print(sort_list)
        for i in range(len(sort_list)):
            for node in list[sort_list[i][0]]:
                b.write(node+"\t")
            b.write("\n")




