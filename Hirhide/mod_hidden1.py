class Modularity(object):
    def __init__(self):

        """
        Constructor
        """

    def execute(self,test,truth_F,base,graphfile):
        #test为传入的社团
        Mate = open(base+ "/result/Mate.txt", "r")
        correspond = open(base + "/correspond.txt", "r")
        graph = open(base + "/" + graphfile + ".txt", "r")
        ModHidden_protein = open(base+ "/result/ModHidden_protein.txt", "w")
        Detected_protein = open(base + "/result/Detected_protein.txt", "w")
        Truth_protein = open(base + "/result/Truth_protein.txt", "w")

        lenoftruth=len(truth_F)

        modvalue=self.Modvalue(test,graph)
        hiddenness = self.get_hiddenness(modvalue, test)
        '''print("modvalue")
        print(modvalue)
        print(len(modvalue))

        print("hiddenness")
        print(hiddenness)
        print(sum(hiddenness)/len(test))'''

        #筛选处于hiddenness layer中的社团
        id_layer=self.classify(test)

        assert len(id_layer)==1

        ##################################################
        #筛选modularity value较大的社团
        id_match=[]
        id_unmatch=[]
        sum_mod=0
        #print("test1")
        print(len(test))
        Mate_all = []
        for Mate_read in Mate:
            Mate_read = Mate_read.strip().split()
            print(Mate_read)
            Mate_all.append(Mate_read)
        Mate_hi=Mate_all[0]
        Mate_mod = Mate_all[3]

        #id_detected的下标即为detected的下标
        id_detected=Mate_hi[lenoftruth:]

        '''print(id_detected)
        print("id_detected")
        print(len(id_detected))'''

        for i in range(len(id_detected)):
            if id_detected[i]!='-1':
                id_match.append(i)
                sum_mod+=modvalue[i]
            else:
                id_unmatch.append(i)
    # 找出与truth相匹配的社团的modularity的平均值
        average_mod=sum_mod/len(id_match)
        #print(average_mod)
        id_filter_mod=[]
        for id in id_unmatch:
            if modvalue[id]>average_mod:
                id_filter_mod.append(id)
        print(id_filter_mod)
    # 筛选hiddenness value较大的社团
        id_filter_modhid=[]
        for i in id_filter_mod:
            if hiddenness[i]>sum(hiddenness)/len(hiddenness) and i>=id_layer[0]:
                id_filter_modhid.append(i)
        #print("id_filter_modhid")
        print(id_filter_modhid)
        #test_protein=[]
    #将编号转化为protein id
        correspond_list={}
        for item in correspond:
            item=item.strip().split()
            correspond_list[item[0]]=item[1]
        print(correspond_list)
        print(id_detected)
        print("id_detected")
        print(len(id_detected))
        for id in id_filter_modhid:
            for i in test[id]:
                ModHidden_protein.write(correspond_list[str(i)]+"\t")
            ModHidden_protein.write("\n")
            # id_detected[id]中存的是truth_F的序号
        mod_detected = open(base + "/mod_merge.gen", "r")
        mod_list = self.get_list(mod_detected)
        truth = Mate_hi[:lenoftruth]
        truth_mod=Mate_mod[:lenoftruth]
        d=[]
        m=[]
        t1=[]
        t_input=[]
        for i in range(len(truth_mod)):
            if truth_mod[i]!='-1' and truth[i]!="-1":
                num1 = int(truth[i]) - lenoftruth
                num2=int(truth_mod[i])-lenoftruth
                d.append(test[num1])
                m.append(mod_list[num2])
                t_input.append(truth_F[i])
        for i in range(len(truth)):
            if truth[i]!='-1':
                num=int(truth[i])-lenoftruth
                t1.append(truth_F[i])
                for k in test[num]:
                    Detected_protein.write(correspond_list[str(k)] + "\t")
                Detected_protein.write("\n")
                for j in truth_F[i]:
                    Truth_protein.write(correspond_list[str(j)] + "\t")
                Truth_protein.write("\n")
            else:
                Detected_protein.write("0" + "\n")
                Truth_protein.write("0" + "\n")
        print("t1 and t2###########################3")
        print(d)
        print(m)

        sort1=self.get_recall_line(t_input,base,graphfile)
        sort2=self.get_recall_line(t_input,base, graphfile)
        print("sort1 and sort2")
        print(sort1)
        accuracy1=self.get_accuracy(sort1,t_input,d)
        accuracy2=self.get_accuracy(sort2, t_input, m)
        accuracy = open(base + "/result/accuracy.txt", "w")
        for item in accuracy1:
            accuracy.write(str(item)+"\t")
        accuracy.write("\n")
        for item in accuracy2:
            accuracy.write(str(item)+"\t")
#################################################################################
    def get_recall_line(self,t,base,graphfile):
        graph1 = open(base + "/" + graphfile + ".txt", "r")
        modvalue_truth = self.Modvalue(t, graph1)
        hiddenness_truth = self.get_hiddenness(modvalue_truth, t)
        #print("hiddenness")
        #print(hiddenness_truth)
        h = []
        count=0
        for i in range(len(hiddenness_truth)):
            one = [i, hiddenness_truth[i]]
            h.append(one)
            if hiddenness_truth[i]!=1 and hiddenness_truth[i]!=0:
                count+=1

        increase = sorted(h, key=lambda x: x[1], reverse=False)
        print("increase")
        print(increase)
        sort=[]
        for i in range(len(increase)):
            sort.append(increase[i][0])
        return sort

    def get_list(self, file):
        list=[]
        for line in file:
            line=line.strip().split()
            list.append(line)
        return list

    def get_accuracy(self, sort, truth, detected):
        if len(truth)==len(detected):
            print("@@@@@@@@@@@@@@@@@@@@@")
            accuracylist=[]
            for i in range(len(truth)):
                if detected[i]!=0:
                    inter=set(truth[i])&set(detected[i])
                    union=set(truth[i])|set(detected[i])
                    accuracy=len(inter)/len(union)
                    accuracylist.append(accuracy)
            accuracysort=[]
            print("@@@@@@@@@@@@@@@@@@@@@")
            for item in sort:
                accuracysort.append(accuracylist[item])
            print(accuracysort)
            return accuracysort







                    #test_protein.append(correspond_list[str(i)])
            #print(test_protein)

    def classify(self, detected):
        id_layer = []
        for i in range(len(detected)):
            if len(id_layer)==1:
                continue
            indice = 0
            if i > 20:
                for k in range(i - 23, i - 3):
                    if len(detected[i]) < len(detected[k]) + 5:
                        indice = 1
            if indice == 0 and i > 60:
                id_layer.append(i)
        return id_layer
#L_detected_F
    def Modvalue(self,test, graph):
        print("test")
        print(len(test))

        ###############modularity of test communities##################
        nodes = set()
        for community in test:
            for node in community:
                nodes.add(node)
        graph_F = []
        for item in graph:
            item = item.strip().split()
            if item[0] in nodes and item[1] in nodes:
                graph_F.append(item)
        ####get e####
        print("graph_F")
        print(graph_F)
        e = len(graph_F)
        print(e)

        ComOfNode = {}
        ModofCom = []
        for node in nodes:
            k = 0
            # ComOfNode[node]=[]
            for i in range(len(test)):
                if node in test[i]:
                    k += 1
                    # ComOfNode[node].append(i)
            ComOfNode[node] = k
        count=0
        for i in range(len(test)):
            e_kk=0
            e_kout=0
            for pair in graph_F:
                ##################### get e_kk #####
                if pair[0] in test[i] and pair[1] in test[i]:
                    A1 = float(pair[2])
                    W_ik = 1 / ComOfNode[pair[0]]
                    W_jk = 1 / ComOfNode[pair[1]]
                    d1 = 0.25 * (W_ik + W_jk) * A1
                    e_kk += d1
                ###################### get d_k #####
                if (pair[0] in test[i] and pair[1] not in test[i]):
                    A2 = float(pair[2])
                    W_ik = 1 / ComOfNode[pair[0]]
                    W_jk = 1 / ComOfNode[pair[1]]
                    d2 = 0.25 * (W_ik + 1 - W_jk) * A2
                    e_kout += d2
                if (pair[1] in test[i] and pair[0] not in test[i]):
                    A2 = float(pair[2])
                    W_ik = 1 / ComOfNode[pair[1]]
                    W_jk = 1 / ComOfNode[pair[0]]
                    d3 = 0.25 * (W_ik + 1 - W_jk) * A2
                    e_kout += d3

            d_k = 2 * e_kk + e_kout
            Q = e_kk / e - (d_k / (2 * e)) ** 2
            Ck = len(test[i])
            #ModofCom.append(Q / Ck)
            #ModofCom.append(round(Q,2))
            ModofCom.append(Q)

            if Q>0:
                count+=1
        sumQ=sum(ModofCom)
        print(sumQ)
        print(count)
        print("MODofCOM")
        print(len(ModofCom))
        return ModofCom

    def get_hiddenness(self,ModofCom,test):
        hiddenness=[]
        for i in range(len(test)):
            #section=0
            total=set()
            Ck=len(test[i])
            for j in range(len(test)):
                if ModofCom[j]>ModofCom[i]:
                    inter=set(test[j])&set(test[i])
                    #k=[item1 for item1 in test[i] for item2 in test[j] if item1==item2]
                    for item in inter:
                        total.add(item)
                    #section+=k
            hiddenness.append(round(len(total)/Ck,2))
        return hiddenness


