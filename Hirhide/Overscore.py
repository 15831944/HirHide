#预处理的时候需要留下多少个 每个complex需要留下多少个蛋白质
from mwmatching import maxWeightMatching
import math
class Overscore(object):

    def __init__(self):
        """
        Constructor
        """
    def execute(self, base,L_truth_F,L_detected_F,overscore,overscore_F,item):
        Mate = open(base + "/result/Mate"+item, "w")
        truth_L = len(L_truth_F)
        detected_L = len(L_detected_F)

        # 计算MMR
        MMR,mates = self.M_M_R(L_truth_F,L_detected_F)
        print("mates:")
        print(mates)
        print(len(mates))
        print(len(L_truth_F))
        print(len(L_detected_F))
        print("MMR: %f"%MMR)
    ###########################################################################


        #计算standarized recall

        recall_list=[]
        for i in range(truth_L):
            r_list=[]
            for j in range(detected_L):
                both = set(L_detected_F[j]) & set(L_truth_F[i])
                union=set(L_detected_F[j]) | set(L_truth_F[i])
                r=len(both)/len(union)
                r_list.append(r)
            recall=max(r_list)
            recall_list.append(recall)
        Recall=sum(recall_list)/len(recall_list)

        '''# 计算Fraction of matched complexes
        count=0
        for i in range(truth_L):
            i_indice=0
            for j in range(detected_L):
                both=set(L_detected_F[j])&set(L_truth_F[i])
                w=len(both)*len(both)/( len(L_detected_F[j])*len(L_truth_F[i]) )
                if w > 0.5:
                    i_indice=1
            count+=i_indice
        Fraction=count/truth_L
        print("Fraction: %f"%Fraction)'''




    ###########################################################################
        a = str(round(Recall, 2))
        b = str(round(MMR, 2))
        #c = str(round(Fraction, 2))
        d = str(round(Recall +  MMR, 2))
        overscore.write(d + "\n")
        overscore.write(b + ","  + a + "\n")
        overscore_F.write("["+b + "," + a + "], ")
        for item in mates:
            Mate.write(str(item)+"\t")
        Mate.write("\n")
        #Mate.write("\n"+"############################################"+"\n")
        #print("overscore(Recall, MMR): %.2f,%.2f" % (Recall, MMR))


    ###########################################################################
    #获取交集之后的truth和detected
    def Filter(self,truth, detected):
        truth_F=[]
        detected_F=[]
        for line in truth:
            line=line.strip().split()
            truth_F.append(line)
        print(truth_F)
        for line in detected:
            line=line.strip().split()
            detected_F.append(line)
        print(detected_F)
        return truth_F,detected_F
    ###########################################################################
    def matching_score(self,set1, set2):
        """Calculates the matching score between two sets (e.g., a cluster and a complex)
        using the approach of Bader et al, 2001"""
        set_set1=set(set1)
        set_set2=set(set2)
        '''print(" set_set12")
        print(set_set1)
        print(set_set2)'''
        return len(set_set1.intersection(set_set2)) / float(len(set_set1|set_set2))
        #return len(set_set1.intersection(set_set2)) / len(set_set1.union(set_set2))


    def M_M_R(self, truth, detected, score_threshold=0.5):
        scores = {}
        n = len(truth)
        #c1,c2为两个社团，
        for id_truth, c1 in enumerate(truth):
            for id_detected, c2 in enumerate(detected):
                score = self.matching_score(c1, c2)
                if score < score_threshold:
                    #continue
                    scores[id_truth, id_detected + n] = -1

                scores[id_truth, id_detected + n] = score

        input = [(v1, v2, w) for (v1, v2), w in scores.items()]
        mates = maxWeightMatching(input)
        score = sum(scores[i, mate] for i, mate in enumerate(mates) if i < mate)
        return score / n,mates



    def for_truth(self,L_truth_F,L_detected_F):
        indice_pair = {}
        score = {}
        truth_L = len(L_truth_F)
        detected_L = len(L_detected_F)
        for i in range(truth_L):
            scorei=[0,0]
            pair=[-1,-1]
            for j in range(detected_L):
                both=set(L_detected_F[j]) & set(L_truth_F[i])
                weight=len(both)*len(both)/( len(L_detected_F[j])*len(L_truth_F[i]) )
                if weight>scorei[0]:
                    #储存权重最大的两条边
                    scorei[1]=scorei[0]
                    scorei[0]=weight
                    #储存两条边对应的社团编号
                    pair[1]=pair[0]
                    pair[0]=j
            indice_pair[i]=pair
            score[i]=scorei
        return indice_pair,score

    def for_detected(self,L_truth_F,L_detected_F):
        indice_pair = {}
        score = {}
        truth_L = len(L_truth_F)
        detected_L = len(L_detected_F)
        for i in range(detected_L):
            scorei=[0,0]
            pair=[-1,-1]
            for j in range(truth_L):
                both=set(L_detected_F[i]) & set(L_truth_F[j])
                weight=len(both)*len(both)/( len(L_detected_F[i])*len(L_truth_F[j]) )
                if weight>scorei[0]:
                    #储存权重最大的两条边
                    scorei[1]=scorei[0]
                    scorei[0]=weight
                    #储存两条边对应的社团编号
                    pair[1]=pair[0]
                    pair[0]=j
            indice_pair[i]=pair
            score[i]=scorei
        return indice_pair,score

    def Collision(self, indice_pair):
        collision=[]
        collection_co=set()
        for i in range(len(indice_pair)):
            collisioni=[i]
            collection_co.add(i)
            for j in range(len(indice_pair)):
                if indice_pair[i][0]==indice_pair[j][0] and j not in collection_co:
                    collisioni.append(j)
                    collection_co.add(j)
            if len(collisioni)>1:
                collision.append(collisioni)
        return collision

    ###########################################################################

    def modularity(self,test, graph):

        ###############modularity of test communities##################3
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
        e = len(graph_F)

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
        count = 0
        for i in range(len(test)):
            e_kk = 0
            e_kout = 0
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
            # ModofCom.append(Q / Ck)
            # ModofCom.append(round(Q,2))
            ModofCom.append(Q)

            if Q > 0:
                count += 1
        sumQ = sum(ModofCom)
        print(sumQ)
        print(count)
        print(len(ModofCom))
        return ModofCom

