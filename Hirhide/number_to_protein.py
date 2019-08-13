def excute(base,graphfile,correspond,type):
    # test为传入的社团
    file = open(base + "/" + graphfile + ".txt", "r")
    protein = open(base + "/" + graphfile + "_"+type+"_protein.txt", "w")
    correspond_list=[]
    protein_list=[]
    for line in correspond:
        line=line.strip().split()
        correspond_list.append(line[1])
    for line in file:
        p_line=[]
        line=line.strip().split()
        line=line[:2]
        p_line.append(correspond_list[ int( line[0] ) ] )
        p_line.append(correspond_list[ int( line[1] ) ] )
        protein_list.append(p_line)
    #print(protein_list)
    for item in protein_list:
        protein.write(item[0]+"\t"+item[1]+"\n")

