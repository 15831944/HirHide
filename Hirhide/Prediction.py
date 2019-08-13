#预处理的时候需要留下多少个 每个complex需要留下多少个蛋白质

def excute(base,L_truth_F,L_detected_F,al,correspond,graphfile):
    Mate = open(base + "/result/Mate" + al, "r")
    ep=open(base + "/result.txt", "r")
    Predict=open(base + "/Predict"+al, "w")
    l=len(L_truth_F)
    ####change id to protein name###
    detect_proteinl=[]
    for item in L_detected_F:
        detect_protein=[correspond[int(id)][1] for id in item]
        detect_proteinl.append(detect_protein)
    Mate_list=[]
    for item in Mate:
        item = item.strip().split()
        Mate_list.append(item)
    mate=Mate_list[0]
    conditionofdetected=mate[l:]
    predictioncandidate=[]
    for i in range(len(conditionofdetected)):
        if conditionofdetected[i]=="-1":
            predictioncandidate.append(detect_proteinl[i])
    ep_list=[]
    for line in ep:
        line = line.strip().split()
        ep_list.append(line)
    prediction=[]

    for item1 in predictioncandidate:
        item1=set(item1)
        for item2 in ep_list:
            item2=set(item2)
            inter=item1&item2
            union=item1|item2
            thre=len(inter)/len(union)
            #if thre > 0.6 :
            if thre>0.6 and len(item1)>3:
                prediction.append(list(item1))
    prediction_new=[]
    for i in range(len(prediction)):
        if prediction[i] not in prediction_new:
            prediction_new.append(prediction[i])

    for item in prediction_new:
        for protein in item:
            Predict.write(protein+"\t")
        Predict.write("\n")

    ################################
    graph = open(base + "/"+graphfile+"_protein.txt", "r")
    graph_list=[]
    for line in graph:
        line=line.strip().split()
        graph_list.append(line)

    print("prediction")
    print(prediction)
    print("graph_list")
    print(graph_list)
    for i in range(len(prediction)):
        nodes=open(base + "/"+"result/"+al+"/"+str(i)+"nodes.csv","w")
        edges=open(base + "/"+"result/"+al+"/"+str(i)+"edges.csv","w")
        nodes.write("Id, lable, name" + "\n")
        edges.write("Source, Target, Type" + "\n")
        edges_list=[]
        for j in range(len(prediction[i])):
            nodes.write(prediction[i][j]+", "+prediction[i][j]+", "+prediction[i][j]+ "\n")
            for k in range(len(prediction[i][j+1:])):
                for item in graph_list:
                    if (prediction[i][j]==item[0] and prediction[i][k]==item[1]) :#or (prediction[i][j]==item[1] and prediction[i][k]==item[0]):
                        #if [prediction[i][k],prediction[i][j]] not in edges_list:
                        edges_list.append([prediction[i][j],prediction[i][k]])

        print("edges_list")
        print(edges_list)
        edges_new=[]
        for item in edges_list:
            if [item[1],item[0]] not in edges_list:
                edges_new.append(item)
        for item in edges_new:
            edges.write(item[0] + ", "+item[1]+", "+"Undirected"+"\n")







