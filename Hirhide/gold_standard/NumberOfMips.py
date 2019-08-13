Mips=open("mips_3_100.txt","r")
number=[]
for line in Mips:
	l_line=line.strip().split()
	for item in l_line:
		if item not in number:
			number.append(item)
print(len(number))

