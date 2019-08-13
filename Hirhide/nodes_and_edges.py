def execute(base,graphfile,nodes_and_edges):
    file=open(base+"/"+graphfile+".txt","r")

    edges=0
    nodeset=set()
    for line in file:
        edges+=1
        line=line.strip().split("\t")
        nodeset.add(line[0])
        nodeset.add(line[1])
    nodes=len(nodeset)
    nodes_and_edges.write(base+"\t"+graphfile+"\t"+"\n")
    nodes_and_edges.write(str(nodes)+"\t"+str(edges)+"\n")
