##ͼ�ļ���ʽ
��ͼ�ļ��ŵ�Ŀ¼�У���������Ϊgraph ����չ��
graph�ļ���ʽΪ��
��һ�п�ѡ������ ��ʡ��
����ÿ�б�ʾһ���ߣ��ɴ�Ȩ����Ȩ
���磺
```
3000
1 2 1
1 11 1
1 14 1
1 18 1
1 24 1
```
```
1 2 1
1 11 1
1 14 1
1 18 1
1 24 1
```
```
3000
1 2
1 11
1 14
1 18
1 24
```
```
1 2
1 11
1 14
1 18
1 24
```
##ʹ�÷�����
run.exe F:/HICODE_SUB/syn/runtest/ mod infomap
��ͼ F:/HICODE_SUB/syn/3000/graph �����㷨mod��infomap�����н����ŵ�F:/HICODE_SUB/syn/3000/baseline/Ŀ¼��
mod = false, infomap = false;
demon = false, lc = true;
oslom = false, gce = false, cfinder = false;
bool oslom = false, gce = false, cfinder = false;
bool oslom = false, gce = false, cfinder = false;
bool oslom = false, gce = false, cfinder = false;





###########################
#####    HirHide     #######
###########################

#truth�ļ�
#truth=truth1.gen;truth2.gen
truth=truth.txt

#���߷��� ��ѡ:ReduceWeight;Remove
reduce_method=ReduceWeight
use_leaf_community_reduce=false

#���㷨 �Ƽ���mod;infomap ��ѡ��oslom;demon;lc;gce;cfinder
base_alg=mod
output_baseline_results=true

#����
number_of_layers=3

#��������
number_of_iteration=20



#�Ƿ����log��Ϣ

#����ÿ�ε�����modularityֵ
log_modularity=true

#���ÿ�ε�������仯
log_nmi_last=true

#ÿ�ε������浱ʱ���õ����ߺ��ͼ
log_save_reduce_graph=false


###########################
#####      sub      #######
###########################

#ʹ�õݹ�ץ��ͼ������
use_r_sub=true

#�ݹ����
sub_times=2

#�ڵ������������ֲŵݹ�ץ��ͼ
sub_nodes_number_thres=9

#maxOri��maxLayer
sub_maxori=true
sub_maxlayer=false



