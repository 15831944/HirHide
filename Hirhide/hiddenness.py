import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
def execute(base,graphfile,type,item):

    accuracy = open(base+"/result/accuracy"+item, "r")
    il=40


    '''#if graphfile=="biogrid_yeast_physical_unweighted" and type=="mips":
    il=12 #interval间隔
    end=120
    if graphfile=="biogrid_yeast_physical_unweighted" and type== "cyc":
        il=15 #interval间隔
        end=150
    if graphfile=="YeastNet" and type== "cyc":
        il=16 #interval间隔
        end=160
    if graphfile=="YeastNet" and type=="mips":
        il=5 #interval间隔
        end=95
    if graphfile=="krogan2006_core" and type== "cyc":
        il=5 #interval间隔
        end=85
    if graphfile=="krogan2006_core" and type=="mips":
        il=1 #interval间隔
        end=19'''
    def get_average(list):
        list_new=[]
        print(len(list))
        for i in range(int(len(list) / il)):
            sumil = sum(list[il * i:il * (i+ 1)])
            list_new.append(sumil / il)
        return list_new

    list = []
    for line in accuracy:
        line = line.strip().split("\t")
        list.append(line)
    print("list")
    print(len(list[0]))
    end=len(list[0])-2
    hi=[float(i) for i in list[0][:end]]
    mod=[float(i) for i in list[1][:end]]
    list1=get_average(hi)
    list2=get_average(mod)

    #x=[i for i in range(len(list[0]))]
    x=[i for i in range(int(len(hi)/il))]
    y1=[float(i) for i in list1]
    y2=[float(i) for i in list2]
    x=np.array(x)
    y1=np.array(y1)
    y2=np.array(y2)
    x_new = np.linspace(x.min(), x.max(), 200)
    y_new1 = spline(x, y1, x_new)
    y_new2 = spline(x, y2, x_new)
    #x_new = np.linspace(x.min(), x.max(), )
    #x_mod=np.array(x_mod)
    plt.figure(figsize=(7,3))
    plt.xlabel("Communities")
    plt.ylabel("Accuracy")
    if item=="HiHiCode-MOD.txt":
        plt.plot(x_new, y_new1, label="HiHiCode-MOD", linewidth='1.5', color="#FF0000")
        plt.plot(x_new, y_new2, label="MOD", linewidth='1.5', color="#000000")
        plt.xticks([])
        # plt.ylim(0.0, 0.5)
        plt.yticks([])
        #plt.yticks(np.linspace(0.2, 0.8, 7, endpoint=True))
        plt.legend(loc='lower right')
        plt.savefig(base+"/hiddenness1.pdf")
    if item=="HiHiCode-Infomap.txt":
        plt.plot(x_new, y_new1, label="HiHiCode-Infomap", linewidth='1.5', color="#FF0000")
        plt.plot(x_new, y_new2, label="Infomap", linewidth='1.5', color="#000000")
        plt.xticks([])
        # plt.ylim(0.0, 0.5)
        plt.yticks([])
        #plt.yticks(np.linspace(0.2, 0.7, 6, endpoint=True))
        plt.legend(loc='lower right')
        plt.savefig(base+"/hiddenness2.pdf")
    if item=="HiHiCode-LC.txt":
        plt.plot(x_new, y_new1, label="HiHiCode-LC", linewidth='1.5', color="#FF0000")
        plt.plot(x_new, y_new2, label="LC", linewidth='1.5', color="#000000")
        plt.xticks([])
        # plt.ylim(0.0, 0.5)
        plt.yticks([])
        #plt.yticks(np.linspace(0, 0.6, 7, endpoint=True))
        plt.legend(loc='lower right')
        plt.savefig(base+"/hiddenness3.pdf")
    #plt.show()
