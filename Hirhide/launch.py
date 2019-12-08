import Overscore as OS
import mod_hidden as MOD
import truth_detected_graph as TDG
import Metric_Figure as MF
import get_MOD_nodes as GMN
import hiddenness as HI

########################## Change ##########################
MF.excute() #生成各种评价标准下各个算法的准确度的柱状图
########################## Change ##########################

graphfiles=["biogrid_yeast_physical_unweighted", "YeastNet", "krogan2006_core"]
#graphfiles=["YeastNet"]
#graphfiles=["krogan2006_core"]
#graphfiles=["biogrid_yeast_physical_unweighted"]
for graphfile in graphfiles:
    print("\n")
    print("####################")
    print("\n")
    print("开始运行数据集：%s"%graphfile)

    ########################## Change ##########################
    #algorithm_result=["HiHiCode.txt","Infomap.gen","CFinder.gen","mod_merge.gen","OSLOM.gen"]
    algorithm_result = ["HiHiCode.txt"]
    #algorithm_result = ["mod_merge.gen"]
    for item in algorithm_result:
        print("\n")
        print("####################")
        print("\n")
        print("开始运行算法：%s"%item)
        types=["_cyc/","_mips/"]
        for type in types:
            print("开始运行关于%s的数据集" % type)
            base="dataset"+type+graphfile
            truth = open(base+ "/truth", "r")
            correspond = open(base + "/correspond.txt", "r")
            detected=open(base+"/"+item,"r")#修改此处来改变算法
            overscore = open(base + "/result/Overscore.txt", "a")
            Mate=open(base + "/result/Mate.txt", "a")
            LOS=OS.Overscore()
            truth_F, detected_F = LOS.Filter(truth, detected)
            MO = MOD.Modularity()
            TD=TDG.Truth_detected_graph()
            #MM=MODM.Modularity1()
            def metric():
                overscore.write(item + "\t")
                LOS.execute(truth_F, detected_F, overscore, Mate)

            def mod_hiddenness():
                if item == "HiHiCode.txt" :
                    MO.execute(detected_F,truth_F,base,graphfile)
                #if item == "mod_merge.gen":
                 #   MO.execute(detected_F,truth_F,base,graphfile,item)
            def truth_detected_graph():
                if item == "HiHiCode.txt":
                    #if (graphfile=="biogrid_yeast_physical_unweighted") or (graphfile=="krogan2006_core" and type=="_mips/") or (graphfile=="YeastNet" and type=="_cyc/"):
                    if graphfile=="krogan2006_core" and type=="_cyc/":
                        TD.execute(base,graphfile,truth_F)
            def get_mod_nodes():
                if item == "mod_merge.gen":
                    GMN.execute(truth_F,base)



            ########################################
            #Choose one
            #metric()  #计算各种评价标准下各个算法的准确度
            #get_mod_nodes() #写出mod算法中对应的社团
            #mod_hiddenness()  # 只与hiHICODE检测出来的社团有关，确定他们的modularity和hiddenness value，以及挑选出合适的社团
            #truth_detected_graph()  # 生成选出的蛋白质复合物最终的图像
            #HI.execute(base,graphfile,type)




