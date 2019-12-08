import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
def execute(base,graphfile,type):
    accuracy = open(base+"/result/accuracy.txt", "r")
    if graphfile=="biogrid_yeast_physical_unweighted" and type== "_cyc/":
        il=23 #interval间隔
        end=230
    if graphfile=="biogrid_yeast_physical_unweighted" and type=="_mips/":
        il=40 #interval间隔
        end=200
    if graphfile=="YeastNet" and type== "_cyc/":
        il=21 #interval间隔
        end=210
    if graphfile=="YeastNet" and type=="_mips/":
        il=24 #interval间隔
        end=192
    if graphfile=="krogan2006_core" and type== "_cyc/":
        il=15 #interval间隔
        end=150
    if graphfile=="krogan2006_core" and type=="_mips/":
        il=15 #interval间隔
        end=150
    def get_average(list):
        list_new=[]
        print(len(list))
        for i in range(int(len(list) / il)):
            sumil = sum(list[il * i:il * (i+ 1)])
            list_new.append(sumil / il)
        return list_new

    list=[]
    for line in accuracy:
        line=line.strip().split("\t")
        list.append(line)
    print(len(list[0]))
    print(len(list[1]))
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
    plt.figure(figsize=(7,3.5))
    plt.plot(x_new,y_new1,label="HiHiCode",linewidth = '1.5',color="#FF0000")
    plt.plot(x_new,y_new2,label="MOD",linewidth = '1.5',color="#000000")
    plt.xticks([])
    #plt.ylim(0.0, 0.5)
    plt.yticks(np.linspace(0.25, 0.5, 6, endpoint=True))
    plt.legend(loc='upper right')
    plt.savefig(base+"/hiddenness5.pdf")
    #plt.show()

