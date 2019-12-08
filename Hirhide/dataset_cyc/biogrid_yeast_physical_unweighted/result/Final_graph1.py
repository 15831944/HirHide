import networkx as nx                   #导入NetworkX包，为了少打几个字母，将其重命名为nx
import matplotlib.pyplot as plt
#graphfiles=["biogrid_yeast_physical_unweighted","collins2007","gavin2006_socioaffinities_rescaled","krogan2006_core","krogan2006_extended"]
#graphfiles=["collins2007"]
#graphfiles=["krogan2006_core"]
#graphfiles=["gavin2006_socioaffinities_rescaled"]
graphfile=["biogrid_yeast_physical_unweighted"]
file_read = open("dataset/" + graphfile + "/result/biogrid_yeast_physical_unweighted.txt", "w")
file_color = open("dataset/" + graphfile + "/result/color.txt", 'r')
G = nx.Graph() #首先建一个网络图，此时图中为空
matrix = [[0 for x in range(9)] for y in range(9)]
i = 0
line_num=0
v=[]
for line in file_read: #读入每一行
    line_num+=1
    if line_num==1:
        v[0]=line.split(' ')
    if line_num!=1:
        matrix[i] = line.split(' ')   #将每一行按空格分割
        i = i + 1
                     #建立一个空的无向图

#G.add_nodes_from(v[0])                #从v中添加结点，相当于顶点编号为1到8
line = file_color.read()  #对于一行的数据，可以直接这样读
colors = line.strip().split(' ')
for i in range(len(colors)):
    colors[i] = int(colors[i])
for x in range(0, len(matrix)):    #添加边
    for y in range(0, len(matrix)):
         if matrix[x][y] == '1':
              G.add_edge(x, y)
position={1:(1,0),2:(2,0),3:(3,0),4:(4,0)}#,5:(5,0),6:(6,0),7:(7,0),8:(8,0),9:(9,0)}
nx.draw(G)#, pos=position,node_color=colors,with_labels=False)#
plt.show()



