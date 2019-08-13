import Overscore as OS
import mod_hidden as MOD
import truth_detected_graph as TDG
import Metric_Figure as MF
import get_MOD_nodes as GMN
import hiddenness as HI
import nodes_and_edges as NAE
import number_to_protein as NTP
import Prediction as Pre

########################## Change ###########################
MF.excute() #生成各种评价标准下各个算法的准确度的柱状图
########################## Change ##########################

graphfiles=["biogrid_yeast_physical_unweighted", "YeastNet", "krogan2006_core"]
#graphfiles=["YeastNet"]
#graphfiles=["krogan2006_core"]
#graphfiles=["biogrid_yeast_physical_unweighted"]
types=["cyc","mips"]
#types=["mips"]
algorithm_result = ["HirHide-MOD.txt", "MOD.txt","HirHide-Infomap.txt", "Infomap.gen","HirHide-LC.txt", "LC.gen"]
nodes_and_edges = open("nodes_and_edges.txt", "w")
for graphfile in graphfiles:
    print("\n")
    print("####################")
    print("\n")
    print("开始运行数据集：%s"%graphfile)

    ########################## Change ##########################

    #algorithm_result = ["HiHiCode.txt"]
    #algorithm_result = ["mod_merge.gen"]
    for type in types:
        print("\n")
        print("####################")
        print("\n")
        print("开始运行关于%s的数据集" % type)

        base = graphfile + "/" + type
        overscore = open(base + "/result/Overscore.txt", "w")
        overscore_F = open(base + "/result/Overscore_F.txt", "w")
        correspond = open(base + "/correspond.txt", "r")
        correspond_list=[]
        for line in correspond:
            line = line.strip().split()
            correspond_list.append(line)
        ########################## Change ###########################
        #NAE.excute(base,graphfile,nodes_and_edges)
        #NTP.excute(base,graphfile,correspond,type)
        ########################## Change ###########################
        for item in algorithm_result:
            print("开始运行算法：%s" % item)
            truth = open(base+ "/truth", "r")

            detected=open(base+"/"+item,"r")#修改此处来改变算法
            LOS=OS.Overscore()
            truth_F, detected_F = LOS.Filter(truth, detected)
            MO = MOD.Modularity()
            TD=TDG.Truth_detected_graph()
            #MM=MODM.Modularity1()

            def metric():
                overscore.write(item + "\t")
                LOS.execute(base,truth_F, detected_F, overscore,overscore_F,item)

            def mod_hiddenness():
                if item == "HiHiCode-MOD.txt" or item =="HiHiCode-Infomap.txt" or item =="HiHiCode-LC.txt" :
                    MO.execute(detected_F,truth_F,base,graphfile,item)

            def truth_detected_graph():
                if item == "HiHiCode-MOD.txt":
                    #if (graphfile=="biogrid_yeast_physical_unweighted") or (graphfile=="krogan2006_core" and type=="_mips/") or (graphfile=="YeastNet" and type=="_cyc/"):
                    #if graphfile=="krogan2006_core" and type=="_cyc/":
                    TD.execute(base,graphfile,truth_F)
            def hiddenness_graph():
                if item == "HiHiCode-MOD.txt" or item == "HiHiCode-Infomap.txt" or item == "HiHiCode-LC.txt":
                    #if graphfile == "biogrid_yeast_physical_unweighted" and type == "mips":
                    HI.execute(base, graphfile, type, item)
            def pre():
                if item == "HiHiCode-MOD.txt" or item == "HiHiCode-Infomap.txt" or item == "HiHiCode-LC.txt":
                    Pre.excute(base, truth_F, detected_F, item,correspond_list,graphfile)

            def get_mod_nodes():
                if item == "mod_merge.gen":
                    GMN.execute(truth_F,base)



            ########################################
            #Choose one
            #metric()  #计算各种评价标准下各个算法的准确度
            #get_mod_nodes() #写出mod算法中对应的社团
            #mod_hiddenness()  # 只与hiHICODE检测出来的社团有关，确定他们的modularity和hiddenness value，以及挑选出合适的社团
            #truth_detected_graph()  # 生成选出的蛋白质复合物最终的图像
            #hiddenness_graph()
            #pre()





