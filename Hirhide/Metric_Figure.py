import numpy as np
from matplotlib import pyplot as plt
def excute():
    plt.figure(figsize=(12, 6), dpi=120)
    plt.subplot(1,2,1)
    plt.title("Results using CYC data sets as reference", fontsize=10)
    plt.ylim(0.0,1.6)
    plt.yticks(np.linspace(0.0,1.6,5,endpoint=True))
    #size=2
    x1=[1,2,3]
    total_width,n=0.8,5
    width=total_width/n
    x=[a-2*width for a in x1]
    plt.xlim(0.5,3.5)
    plt.xticks(np.linspace(1.0,3.0,3,endpoint=True))
    plt.xticks([1,2,3],["Biogrid","Krogan_core","YeastNet"])
    biogrid_yeast_physical_unweighted =[[0.46,0.48],[0.26,0.26],[0.34,0.37],[0.39,0.38],[0.25,0.27]]
    krogan2006_core =[[0.64,0.59],[0.12,0.12],[0.60,0.48],[0.63,0.55],[0.15,0.21]]
    YeastNet =[[0.45,0.43],[0.37,0.35],[0.46,0.4],[0.45,0.4],[0.18,0.23]]
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
                #"HICODE.txt", "Infomap.gen", "CFinder", "LC.gen", "Mod.gen_level2", "OSLOM.gen"
                if i==0:
                    plt.bar(X, Y,color="#9b0308" , edgecolor="white" ,width=width,label="HiHiCode")
                if i==1:
                    plt.bar(X, Y, color="#d4d20c" , edgecolor="white",width=width,label="Infomap")
                if i == 2:
                    plt.bar(X, Y, color="#1fa335", edgecolor="white", width=width,label="ClusterOne")
                if i==3:
                    plt.bar(X, Y, color="#32b2ec" , edgecolor="white",width=width,label="Mod")
                if i==4:
                    plt.bar(X, Y, color="#9707df", edgecolor="white",width=width,label="OSLOM")
                for a, b in zip(X, Y):
                    if b>0.06:
                        plt.text(a, b - 0.03, '%.2f' % b, ha='center', va='top', fontsize=6)

            elif j == 1:
                if i==0:
                    plt.bar(X, Y, color="#f70810", edgecolor="white",width=width,bottom=test[j-1])
                if i==1:
                    plt.bar(X, Y, color="#f6f41e" , edgecolor="white",width=width,bottom=test[j-1])
                if i == 2:
                    plt.bar(X, Y, color="#77d40c", edgecolor="white", width=width,bottom=test[j-1])
                if i==3:
                    plt.bar(X, Y, color="#92d8ce", edgecolor="white" ,width=width,bottom=test[j-1])
                if i==4:
                    plt.bar(X, Y, color="#996de8" , edgecolor="white",width=width,bottom=test[j-1])
                for a, b,c in zip(X, map(sum,zip(test[j - 1],Y)),Y):
                    plt.text(a, b - 0.03, '%.2f' % c, ha='center', va='top', fontsize=6)


    #plt.text(1.8, 1.8, "top--Maximum matching ratio", fontsize=7.5)
    #plt.text(1.8,1.65, "bottom--Fraction of matched complexes", fontsize=7.5)
    plt.legend(loc='upper right')


    plt.subplot(1, 2, 2)
    plt.title("Results using MIPS data sets as reference",fontsize=10)
    plt.ylim(0.0, 1.6)
    plt.yticks(np.linspace(0.0, 1.6, 5, endpoint=True))
    # size=2
    x1 = [1, 2, 3]
    total_width, n = 0.8, 5
    width = total_width / n
    x = [a - 2 * width for a in x1]
    plt.xlim(0.5, 3.5)
    plt.xticks(np.linspace(1.0, 3.0, 3, endpoint=True))
    plt.xticks([1, 2, 3], ["Biogrid", "Krogan_core", "YeastNet"])
    biogrid_yeast_physical_unweighted = [[0.33, 0.35], [0.19, 0.18], [0.24, 0.27], [0.2, 0.21], [0.19, 0.16]]
    krogan2006_core = [[0.48, 0.46], [0.13, 0.1], [0.4, 0.42], [0.5, 0.44], [0.16, 0.15]]
    YeastNet = [[0.27, 0.3], [0.29, 0.23], [0.27, 0.29], [0.29, 0.28], [0.16, 0.15]]
    input = list(zip(biogrid_yeast_physical_unweighted, krogan2006_core, YeastNet))  # 将同一个算法放在一个列表之内
    print(input)
    plt.ylabel("Composite score")
    for i in range(len(input)):
        a, b, c, = input[i][0], input[i][1], input[i][2]  # ,input[i][4]
        test = list(zip(a, b, c))  # 将同一个评判标准放在一个列表之内
        print(test)
        for j in range(len(test)):
            X = [item + i * width for item in x]
            Y = test[j]
            if j == 0:
                # "HICODE.txt", "Infomap.gen", "CFinder", "LC.gen", "Mod.gen_level2", "OSLOM.gen"
                if i == 0:
                    plt.bar(X, Y, color="#9b0308", edgecolor="white", width=width, label="HiHiCode")
                if i == 1:
                    plt.bar(X, Y, color="#d4d20c", edgecolor="white", width=width, label="Infomap")
                if i == 2:
                    plt.bar(X, Y, color="#1fa335", edgecolor="white", width=width, label="ClusterOne")
                if i == 3:
                    plt.bar(X, Y, color="#32b2ec", edgecolor="white", width=width, label="Mod")
                if i == 4:
                    plt.bar(X, Y, color="#9707df", edgecolor="white", width=width, label="OSLOM")
                for a, b in zip(X, Y):
                    if b > 0.06:
                        plt.text(a, b - 0.03, '%.2f' % b, ha='center', va='top', fontsize=6)

            elif j == 1:
                if i == 0:
                    plt.bar(X, Y, color="#f70810", edgecolor="white", width=width, bottom=test[j - 1])
                if i == 1:
                    plt.bar(X, Y, color="#f6f41e", edgecolor="white", width=width, bottom=test[j - 1])
                if i == 2:
                    plt.bar(X, Y, color="#77d40c", edgecolor="white", width=width, bottom=test[j - 1])
                if i == 3:
                    plt.bar(X, Y, color="#92d8ce", edgecolor="white", width=width, bottom=test[j - 1])
                if i == 4:
                    plt.bar(X, Y, color="#996de8", edgecolor="white", width=width, bottom=test[j - 1])
                for a, b, c in zip(X, map(sum, zip(test[j - 1], Y)), Y):
                    plt.text(a, b - 0.03, '%.2f' % c, ha='center', va='top', fontsize=6)

    #plt.text(1.8, 1.8, "top--Maximum matching ratio", fontsize=7.5)
    #plt.text(1.8, 1.65, "bottom--Fraction of matched complexes", fontsize=7.5)
    plt.legend(loc='upper right')

    plt.savefig('F:\ClusterOne\Benchmark_results3.pdf')
    plt.show()






