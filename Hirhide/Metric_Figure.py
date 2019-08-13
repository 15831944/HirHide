import numpy as np
from matplotlib import pyplot as plt
def excute():
    figure1()
    figure2()
def figure1():
    plt.figure(figsize=(10, 4), dpi=120)
    #plt.subplot(2,1,1)
    plt.title("Results using CYC data sets as reference", fontsize=10)
    plt.ylim(0.0,1.6)
    plt.yticks(np.linspace(0.0,1.8,5,endpoint=True))
    #size=2
    x1=[1,2,3]
    total_width,n=0.9,6
    width=0.1
    x=[a-2.9*width for a in x1]
    plt.xlim(0.5,3.6)
    plt.xticks(np.linspace(1.0,3.6,3,endpoint=True))
    plt.xticks([1,2,3],["Biogrid","Krogan_core","YeastNet"])
    biogrid_yeast_physical_unweighted =[[0.53,0.47], [0.39,0.39], [0.47,0.39], [0.27,0.26], [0.25,0.16], [0.23,0.15]]
    krogan2006_core =[[0.64,0.67], [0.55,0.63], [0.38,0.42], [0.13,0.12], [0.38,0.38], [0.38,0.38]]
    YeastNet =[[0.47,0.39], [0.43,0.42], [0.47,0.39], [0.37,0.37], [0.3,0.19], [0.25,0.16]]

    input=list(zip(biogrid_yeast_physical_unweighted,krogan2006_core,YeastNet))#将同一个算法放在一个列表之内
    print(input)
    plt.ylabel("Composite score")
    for i in range(len(input)):
        a,b,c,=input[i][0],input[i][1],input[i][2]#,input[i][4]
        test=list(zip(a,b,c))#将同一个评判标准放在一个列表之内
        print(test)
        for j in range(len(test)):
            Y=test[j]
            if j == 1:
                #"HiHiCode-MOD.txt", "HiHiCode-Infomap.txt", "HiHiCode-LC.txt",
                if i==0:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y,color="#7D6608" , edgecolor="white" ,width=width,label="HirHide-MOD")
                if i==1:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y, color="#D4AC0D" , edgecolor="white",width=width,label="MOD")
                if i == 2:
                    X = [item + i * width+0.04 for item in x]
                    plt.bar(X, Y, color="#186A3B", edgecolor="white", width=width,label="HirHide-LC")
                if i==3:
                    X = [item + i * width+0.04 for item in x]
                    plt.bar(X, Y,color="#28B463" , edgecolor="white" ,width=width,label="LC")
                if i==4:
                    X = [item + i * width+0.08 for item in x]
                    plt.bar(X, Y, color="#1B4F72" , edgecolor="white",width=width,label="HirHide-Inf")
                if i == 5:
                    X = [item + i * width+0.08 for item in x]
                    plt.bar(X, Y, color="#2E86C1", edgecolor="white", width=width,label="Inf")
                for a, b in zip(X, Y):
                    if b>0.06:
                        plt.text(a, b - 0.03, '%.2f' % b, ha='center', va='top', fontsize=6)

            elif j == 0:
                if i==0:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y, color="#7D6608", edgecolor="white",width=width,bottom=test[j-1])
                if i==1:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y, color="#D4AC0D" , edgecolor="white",width=width,bottom=test[j-1])
                if i == 2:
                    X = [item + i * width + 0.04 for item in x]
                    plt.bar(X, Y, color="#186A3B", edgecolor="white", width=width,bottom=test[j-1])
                if i==3:
                    X = [item + i * width + 0.04 for item in x]
                    plt.bar(X, Y, color="#28B463", edgecolor="white",width=width,bottom=test[j-1])
                if i==4:
                    X = [item + i * width + 0.08 for item in x]
                    plt.bar(X, Y, color="#1B4F72" , edgecolor="white",width=width,bottom=test[j-1])
                if i == 5:
                    X = [item + i * width + 0.08 for item in x]
                    plt.bar(X, Y, color="#2E86C1", edgecolor="white", width=width,bottom=test[j-1])
                for a, b,c in zip(X, map(sum,zip(test[j - 1],Y)),Y):
                    plt.text(a, b - 0.03, '%.2f' % c, ha='center', va='top', fontsize=6)



    #plt.text(1.8, 1.8, "top--Maximum matching ratio", fontsize=7.5)
    #plt.text(1.8,1.65, "bottom--Fraction of matched complexes", fontsize=7.5)
    plt.legend(loc='upper right')
    plt.savefig('F:\ClusterOne\Benchmark_results1.png')
    plt.show()
   #22222222222222222###############################################################################
def figure2():
    #plt.subplot(2,1,2)

    plt.figure(figsize=(10, 4), dpi=120)
    plt.title("Results using MIPS data sets as reference", fontsize=10)
    plt.ylim(0.0, 1.6)
    plt.yticks(np.linspace(0.0, 1.8, 5, endpoint=True))
    # size=2
    x1 = [1, 2, 3]
    total_width, n = 0.9, 6
    width = 0.1
    x = [a - 2.9 * width for a in x1]
    plt.xlim(0.5, 3.6)
    plt.xticks(np.linspace(1.0, 3.6, 3, endpoint=True))
    plt.xticks([1,2,3],["Biogrid","Krogan_core","YeastNet"])
    biogrid_yeast_physical_unweighted =[[0.41,0.34], [0.21,0.2], [0.39,0.32], [0.19,0.19], [0.15,0.08], [0.12,0.07]]
    krogan2006_core =[[0.48,0.52], [0.39,0.5], [0.28,0.3], [0.1,0.12], [0.22,0.31], [0.23,0.31]]
    YeastNet =[[0.36,0.29], [0.3,0.28], [0.35,0.32], [0.25,0.29], [0.2,0.1], [0.17,0.09]]

    input=list(zip(biogrid_yeast_physical_unweighted,krogan2006_core,YeastNet))#将同一个算法放在一个列表之内
    print(input)
    plt.ylabel("Composite score")
    for i in range(len(input)):
        a,b,c,=input[i][0],input[i][1],input[i][2]#,input[i][4]
        test=list(zip(a,b,c))#将同一个评判标准放在一个列表之内
        print(test)
        for j in range(len(test)):
            X = [item + i * width for item in x]
            Y=test[j]
            if j == 0:
                #"HiHiCode-MOD.txt", "HiHiCode-Infomap.txt", "HiHiCode-LC.txt",
                if i==0:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y,color="#7D6608" , edgecolor="white" ,width=width,label="HirHide-MOD")
                if i==1:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y, color="#D4AC0D" , edgecolor="white",width=width,label="MOD")
                if i == 2:
                    X = [item + i * width+0.04 for item in x]
                    plt.bar(X, Y, color="#186A3B", edgecolor="white", width=width,label="HirHide-LC")
                if i==3:
                    X = [item + i * width+0.04 for item in x]
                    plt.bar(X, Y,color="#28B463" , edgecolor="white" ,width=width,label="LC")
                if i==4:
                    X = [item + i * width+0.08 for item in x]
                    plt.bar(X, Y, color="#1B4F72" , edgecolor="white",width=width,label="HirHide-Inf")
                if i == 5:
                    X = [item + i * width+0.08 for item in x]
                    plt.bar(X, Y, color="#2E86C1", edgecolor="white", width=width,label="Inf")
                for a, b in zip(X, Y):
                    if b>0.06:
                        plt.text(a, b - 0.03, '%.2f' % b, ha='center', va='top', fontsize=6)

            elif j == 1:
                if i==0:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y, color="#7D6608", edgecolor="white",width=width,bottom=test[j-1])
                if i==1:
                    X = [item + i * width for item in x]
                    plt.bar(X, Y, color="#D4AC0D" , edgecolor="white",width=width,bottom=test[j-1])
                if i == 2:
                    X = [item + i * width + 0.04 for item in x]
                    plt.bar(X, Y, color="#186A3B", edgecolor="white", width=width,bottom=test[j-1])
                if i==3:
                    X = [item + i * width + 0.04 for item in x]
                    plt.bar(X, Y, color="#28B463", edgecolor="white",width=width,bottom=test[j-1])
                if i==4:
                    X = [item + i * width + 0.08 for item in x]
                    plt.bar(X, Y, color="#1B4F72" , edgecolor="white",width=width,bottom=test[j-1])
                if i == 5:
                    X = [item + i * width + 0.08 for item in x]
                    plt.bar(X, Y, color="#2E86C1", edgecolor="white", width=width,bottom=test[j-1])
                for a, b,c in zip(X, map(sum,zip(test[j - 1],Y)),Y):
                    plt.text(a, b - 0.03, '%.2f' % c, ha='center', va='top', fontsize=6)



    plt.legend(loc='upper right')


    plt.savefig('F:\ClusterOne\Benchmark_results2.png')
    plt.show()






