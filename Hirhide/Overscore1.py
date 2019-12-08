#预处理的时候需要留下多少个 每个complex需要留下多少个蛋白质
from mwmatching import maxWeightMatching
import math
class Overscore(object):

    def __init__(self):
        """
        Constructor
        """
    def execute(self, L_truth_F, L_detected_F,overscore,Mate):
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

        #计算geometric accuracy
        #计算Sn
        #L_truth_F,L_detected_F
        Sn_max=0
        for i in range(truth_L):
            i_insection=[]
            for j in range(detected_L):
                both = set(L_detected_F[j]) & set(L_truth_F[i])
                i_insection.append(len(both))
            Sn_max+=max(i_insection)
        #print(count_truth)
        count_truth = sum([len(item) for item in L_truth_F])
        print("count_truth")
        print(count_truth)
        Sn=Sn_max/count_truth
        print("Sn: %f"%Sn)
        #计算PPV
        all_insection=0
        PPV_max=0
        for i in range(detected_L):
            i_insection=[]
            for j in range(truth_L):
                both = set(L_truth_F[j]) & set(L_detected_F[i])
                L_both=len(both)
                all_insection+=L_both
                i_insection.append(L_both)
            PPV_max+=max(i_insection)
        PPV=PPV_max/all_insection
        print("PPV: %f"%PPV)
        #计算Acc
        Acc=(Sn*PPV)**0.5
        print("Acc: %f"%Acc)


        #计算Fraction of matched complexes
        '''count=0
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

        count = 0
        for i in range(truth_L):
            i_indice = 0
            for j in range(detected_L):
                both = set(L_detected_F[j]) & set(L_truth_F[i])
                union=set(L_detected_F[j]) | set(L_truth_F[i])
                w = len(both)/len(union)
                if w > 0.5:
                    i_indice = 1
            count += i_indice
        Fraction = count / truth_L
        print("Fraction: %f" % Fraction)

    ###########################################################################
        a = str(round(Fraction, 2))
        b = str(round(Acc, 2))
        c = str(round(MMR, 2))
        d = str(round(Fraction + Acc + MMR, 2))
        # over_score=[Fraction,Acc,MMR]
        overscore.write(d + "\n")
        #overscore.write(a + "\t")
        #overscore.write(b + "\t")
        #overscore.write(c + "\n")
        overscore.write(a + "," + b + "," + c + "\n")
        for item in mates:
            Mate.write(str(item)+"\t")
        Mate.write("\n")
        #Mate.write("\n"+"############################################"+"\n")
        print("overscore(Fraction, Acc, MMR): %.2f,%.2f,%.2f" % (Fraction, Acc, MMR))


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
        return len(set_set1.intersection(set_set2)) ** 2 / (float(len(set1)) * len(set2))
        #return len(set_set1.intersection(set_set2)) / len(set_set1.union(set_set2))


    def M_M_R(self, truth, detected, score_threshold=0.16):
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


        """
        #计算H（X）
        HX=0
        for item in L_detected_F:
            px=len(item)
            hx=-px * math.log(px)
            HX+=hx
        HY = 0
        for item in L_truth_F:
            py = len(item)
            hy = -py * math.log(py)
            HY += hy
        # 计算I（X，Y）
        IXY=0
        for item1 in L_detected_F:
            for item2 in L_truth_F:
                pxy=len(set(item1) & set(item2))
                px=len(item1)
                py=len(item2)
                p=pxy/(px*py)
                if p>0:
                    ixy=pxy * math.log(p)
                    IXY+=ixy

        # 计算NMI（X,Y）
        NMI=2*IXY/(HX+HY)
        print("NMI: %f" % NMI)

        """