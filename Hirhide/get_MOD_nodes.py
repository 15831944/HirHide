def execute(truth_F, base):
    # test为传入的社团
    mod_detected=open(base + "/mod_merge.gen", "r")
    Mate = open(base + "/result/Mate.txt", "r")
    correspond = open(base + "/correspond.txt", "r")
    Detected_protein = open(base + "/result/mod_Detected_protein.txt", "w")
    Truth_protein = open(base + "/result/mod_Truth_protein.txt", "w")
    lenoftruth = len(truth_F)
    print("lenoftruth")
    print(lenoftruth)
    test=[]
    for line in mod_detected:
        line = line.strip().split()
        test.append(line)
    print("test")
    print(test)
    print(len(test))
    ##################################################
    # 筛选modularity value较大的社团
    Mate_all=[]
    for Mate_read in Mate:
        Mate_read = Mate_read.strip().split()
        print(Mate_read)
        Mate_all.append(Mate_read)

    #选择与MOD算法有关的Mate
    Mate_mod=Mate_all[3]
    print("Mate_mod")
    print(Mate_mod)
    print(len(Mate_mod))

    id_detected = Mate_mod[lenoftruth:]
    print("id_detected")
    print(id_detected)
    print(len(id_detected))

    # 将编号转化为protein id
    correspond_list = {}
    for item in correspond:
        item = item.strip().split()
        correspond_list[item[0]] = item[1]
    print("correspond_list")
    print(correspond_list)


    truth = Mate_mod[:lenoftruth]
    print("truth")
    print(truth)
    print("truth:%d"%len(truth))
    for i in range(len(truth)):
        if truth[i] != '-1':
            print(int(truth[i]) - lenoftruth)
            for k in test[int(truth[i]) - lenoftruth]:
                Detected_protein.write(correspond_list[str(k)] + "\t")
            Detected_protein.write("\n")
            for j in truth_F[i]:
                Truth_protein.write(correspond_list[str(j)] + "\t")
            Truth_protein.write("\n")
        else:
            Detected_protein.write("0" + "\n")
            Truth_protein.write("0" + "\n")



