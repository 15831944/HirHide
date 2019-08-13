import networkx as nx                   #导入NetworkX包，为了少打几个字母，将其重命名为nx
import matplotlib.pyplot as plt
class Truth_detected_graph(object):
    def __init__(self):

        """
        Constructor
        """

    def execute(self,base,graphfile,truth_F):
        choose_complex=2
        self.truth_detected(base)  #找出合适的蛋白质写入
        #self.Ggraph(base,graphfile,choose_complex)
        #self.Final_graph(base,graphfile,choose_complex)


    def Final_graph(self, base, graphfile,choose_complex):
        algorithms = ["", "mod_"]
        for algorithm in algorithms:
            self.get_node_edges(base,graphfile,algorithm,choose_complex)

    def Ggraph(self,base,graphfile,choose_complex):
        algorithms=["","mod_"]
        for algorithm in algorithms:
            self.get_edge_color(base,graphfile,algorithm,choose_complex)

    def truth_detected(self,base):
        Detected_protein = open(base + "/result/Detected_protein.txt", "r")
        Truth_protein = open(base + "/result/Truth_protein.txt", "r")
        MOD_protein = open(base + "/result/MOD_Detected_protein.txt", "r")
        Detected_choose = open(base + "/result/Detected_choose.txt", "w")
        mod_choose = open(base + "/result/mod_Detected_choose.txt", "w")
        color = open(base + "/result/color.txt", "w")#根据点的不同（在complex1或者complex2）写入不同的颜色
        mod_color=open(base + "/result/mod_color.txt", "w")
        complex_name=open("dataset_cyc/complex_name.txt", "r")
        truth_complex=open("dataset_cyc/truth.txt", "r")
        Detected=[]
        Truth=[]
        truth_list=[]
        for item in truth_complex:
            item = item.strip().split()
            truth_list.append(item)
        name_list = []
        for item in complex_name:
            item = item.strip().split("\t")
            name_list.append(item)

        for item in Detected_protein:
            item=item.strip().split()
            Detected.append(item)
        for item in Truth_protein:
            item=item.strip().split()
            Truth.append(item)
        choose_id=[]
        Detected_choose_list=[]
        Truth_choose_list=[]
        mod_choose_list=[]
        for i in range(len(Detected)):
            a=set(Detected[i])&set(Truth[i])
            b=set(Detected[i])|set(Truth[i])
            #找出它们之中匹配较好的写入
            if 0.5<len(a)/len(b)<1 and len(a)>5 and len(b)<25:
                Detected_choose_list.append(Detected[i])
                Truth_choose_list.append(Truth[i])
                choose_id.append(i)
        list_MOD_protein=[]
        for item in MOD_protein:
            item = item.strip().split()
            list_MOD_protein.append(item)
        for num in choose_id:
            mod_choose_list.append(list_MOD_protein[num])
        print("Truth_choose_list")
        print(Truth_choose_list)
        print(len(Truth_choose_list))
        for i in range(len(Truth_choose_list)):
            for j in range(len(Truth_choose_list)):
                inter=set(Truth_choose_list[i])&set(Truth_choose_list[j])
                if i!=j and 1<len(inter)<6:
                    q=0
                    q_list=[]
                    for k in range(len(truth_list)):
                        a=set(truth_list[k])
                        b1=set(Truth_choose_list[i])
                        b2=set(Truth_choose_list[j])
                        c1=a & b1
                        c2=a & b2
                        d1=a |b1

                        d2=a | b2
                        r1=len(c1)/len(d1)
                        r2=len(c2)/len(d2)

                        if c1==b1 and r1>0.8:
                            #print("@@@@@@@@@@@@@@@@@@@@@@")
                            #print(name_list[k])
                            q+=1
                            q_list.append(name_list[k])

                        if c2==b2 and r2>0.8:
                            #print("@@@@@@@@@@@@@@@@@@@@@@")
                            #print(name_list[k])
                            q+=1
                            q_list.append(name_list[k])

                    if q==2 and q_list!=[['SWI/SNF complex'], ['RSC complex']]:
                        print("@@@@@@@@@@@@@@@@@@@@@@")
                        print(q_list)
                        w1,h1,merge1,color_list1=self.Color(Truth_choose_list[i], Truth_choose_list[j], Detected_choose_list[i],Detected_choose_list[j])
                        w2, h2, merge2 ,color_list2=self.Color(Truth_choose_list[i], Truth_choose_list[j], mod_choose_list[i], mod_choose_list[j])
                        if w1 < 7 and h1 < 7 and len(merge1) > 16: #and w2<10:
                            print("成功写入")
                            print("没有检测到的点")
                            print(h1)
                            for item in merge1:
                                Detected_choose.write(item + "\t")
                            Detected_choose.write("\n")
                            for item in color_list1:
                                color.write(item + "\t")
                            color.write("\n")
                            for item in merge2:
                                mod_choose.write(item + "\t")
                            mod_choose.write("\n")
                            for item in color_list2:
                                mod_color.write(item + "\t")
                            mod_color.write("\n")



    def Color(self,truth_list1,truth_list2,list1,list2):#写入颜色
        all=set(truth_list1)|set(truth_list2)
        truth_inter=set(truth_list1)&set(truth_list2)
        dall=set(list1)|set(list2)
        merge=all|dall
        merge=list(merge)
        color_list = [0 for i in range(len(merge))]
        complex1 = set(truth_list1) - truth_inter
        complex2 = set(truth_list2) - truth_inter
        print("merge and complex1 and complex2 and truth_inter")
        print(len(merge))
        print(complex1)
        print(complex2)
        print(truth_inter)
        w=0
        for n in range(len(merge)):
            if merge[n] in complex1:
                color_list[n] = "g"
            elif merge[n] in complex2:
                color_list[n] = "b"
            elif merge[n] in truth_inter:
                color_list[n] = "y"
            elif merge[n] in list1 and merge[n] not in all:
                color_list[n] = "gp"
                w+=1
            elif merge[n] in list2 and merge[n] not in all:
                color_list[n] = "bp"
                w += 1

        print("检测出的额外的点")
        print(w)
        z=0
        print("##################################")
        for n in range(len(merge)):
            if merge[n] in truth_list1 and merge[n] not in list1:
                print(merge[n])
                z+=1
        print(z)
        print("##################################")
        for n in range(len(merge)):
            if merge[n] in truth_list2 and merge[n] not in list2:
                print(merge[n])
                z+=1
        print(z)
        print("##################################")
        return w,z,merge,color_list















    ####################################################

    def get_edge_color(self,base,graphfile,algorithm,choose_complex):
        graph = open("dataset_row/" + graphfile + ".txt", "r")
        Detected_choose = open(base + "/result/"+algorithm+"Detected_choose.txt", "r")
        #Truth_choose = open(base + "/result/Truth_choose.txt", "r")
        generategraph = open(base + "/result/" +algorithm+graphfile + ".txt", "w")
        graph_list = []
        pair = []
        choose_list=[]
        for line in graph:
            line = line.strip().split()
            graph_list.append(line[:2])
        for line in Detected_choose:
            line = line.strip().split()
            for item in graph_list:
                if item[0] in line and item[1] in line:
                    pair.append(item)
            choose_list.append(line)
        print("choose_list")
        print(choose_list)
        name = choose_list[choose_complex]
        n = len(name)
        for i in range(len(name)):
            generategraph.write(name[i] + "\t")
            # detected和truth中都存在的点：标红
        generategraph.write("\n")
        matric = [[0 for i in range(n)] for i in range(n)]
        for i in range(len(name)):
            for j in range(len(name)):
                for item in pair:
                    if name[i] in item and name[j] in item and i != j:
                        matric[i][j] = 1
                # if [name[i],name[j]] in pair or [name[j],name[i]] in pair:
                #   matric[i][j]=1
        for item in matric:
            for i in item:
                generategraph.write(str(i) + "\t")
            generategraph.write("\n")

     ####################################################



    def get_node_edges(self,base,graphfile,algorithm,choose_complex):
        detect = open(base + "/result/" + algorithm + "Detected_choose.txt", "r")
        edge_read = open(base + "/result/" +algorithm+ graphfile + ".txt", "r")
        color = open(base + "/result/"+algorithm+"color.txt", "r")
        label=open("dataset_cyc/CYC2008.txt")
        nodes = open(base + "/result/node_and_edges/"+algorithm+"nodes.csv", 'w')
        edges = open(base + "/result/node_and_edges/"+algorithm+"edges.csv", 'w')
        nodes.write("Id, lable, name, Modularity Class" + "\n")
        edges.write("Source, Target" + "\n")
        detect_list = []
        color_list = []
        edge_list = []
        label_list=[]
        for line in label:
            line = line.strip().split("\t")
            label_list.append(line[:2])
        for line in edge_read:
            line = line.strip().split()
            edge_list.append(line)
        name_list = edge_list[0]
        edge_row = edge_list[1:]
        for line in color:
            line = line.strip().split()
            color_list.append(line)
        for line in detect:
            line = line.strip().split()
            detect_list.append(line)
        merge = detect_list[choose_complex]
        label_choose=[]
        for i in range(len(merge)):
            for j in range(len(label_list)):
                if merge[i]==label_list[j][0]:
                    label_choose.append(label_list[j][1])
                    break
            nodes.write(str(i)+","+label_choose[i]+","+merge[i]+","+color_list[choose_complex][i]+"\n")
        for i in range(len(edge_row)):
            for j in range(i):
                if edge_row[i][j]=="1":
                    edges.write(str(i)+","+str(j)+"\n")

    #def get_complex_name(self,base,):






