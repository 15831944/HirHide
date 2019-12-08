def Ggraph(graph,Detected_choose,Truth_choose,generategraph,color):
    graph_list=[]
    pair=[]
    detect=[]
    truth=[]
    for line in graph:
        line=line.strip().split()
        graph_list.append(line[:2])
    for line in Detected_choose:
        line = line.strip().split()
        detect.append(line)
        for item in graph_list:
            if item[0] in line and item[1] in line:
                pair.append(item)
        break
    for line in Truth_choose:
        line = line.strip().split()
        truth.append(line)
        for item in graph_list:
            if item[0] in line and item[1] in line:
                if item not in pair:
                    pair.append(item)
        #generategraph.write(item[0]+"\t"+item[1]+"\n")
        break
    name=set(detect[0])|set(truth[0])
    inter=set(detect[0])&set(truth[0])
    color_detect=set(detect[0])-inter
    color_truth=set(truth[0])-inter
    n = len(name)
    color_list=[0 for i in range(n)]

    name=list(name)

    for i in range(len(name)):
        generategraph.write(name[i] + "\t")
        #detected和truth中都存在的点：标红
        if name[i] in inter:
            color_list[i]='r'
        # detected中存在的点：标绿
        if name[i] in color_detect:
            color_list[i]='g'
        # detected中存在的点：标蓝
        if name[i] in color_truth:
            color_list[i]='b'
    generategraph.write("\n")


    matric=[[0 for i in range(n)] for i in range(n)]

    for i in range(len(name)):
        for j in range(len(name)):
            for item in pair:
                if name[i] in item and name[j] in item and i!=j:
                    matric[i][j]=1
            #if [name[i],name[j]] in pair or [name[j],name[i]] in pair:
             #   matric[i][j]=1
    for item in matric:
        for i in item:
            generategraph.write(str(i) + "\t")
        generategraph.write("\n")
    for item in color_list:
        color.write(str(item)+"\t")




