import re

dic_letter = {"A":"1", "C":"2", "T":"3", "G":"4", "a":"1", "c":"2", "t":"3", "g":"4"}
dic_sp = {}

def set_dic_sp(file):
    f = open(file, 'r')
    i = 0
    for line in f.readlines():
        tmp = line.split()
        i += 1
        dic_sp[tmp[0]] = str(i)
    f.close()

# Preparation 
set_dic_sp("../alignment/tree0.terms.embed")

# Step 1, modify alignment
prefix = ""
f = open("../alignment/tree0.terms.embed", 'r')
lines = f.readlines()
prefix = str(len(lines)) + " \t " + str(len(lines[0].split()[1])) + "\n"
f.close()

for i in range(4000):
    f = open("../alignment/tree"+ str(i) +".terms.embed", 'r')
    result = prefix
    for line in f.readlines():
        tmp = line.split()
        result += dic_sp[tmp[0]] + " \t " + " ".join(tmp[1]) + "\n"
        for item in dic_letter:
            result = result.replace(item, dic_letter[item])
    f.close()
    f = open("../alignment/tree"+ str(i) +".terms.embed", 'w')
    f.write(result)
    result = ""

# Step 2, modify trees (i.e graph)
for i in range(4000):
    f = open("../tree/tree"+ str(i) +".taxo", 'r')
    result = ""
    for line in f.readlines():
        tmp = (line.replace("\n", "")).split()
        # print(tmp)
        if tmp[0] in dic_sp:
            tmp[0] = dic_sp[tmp[0]]
        else:
            tmp[0] = "1" + "".join(re.findall('\d+', tmp[0])) + "000"
        if tmp[1] in dic_sp:
            tmp[1] = dic_sp[tmp[1]]
        else:
            tmp[1] = "1" + "".join(re.findall('\d+', tmp[1])) + "000"
        result += tmp[0] + " \t " + tmp[1] + "\n"
    f.close()
    f = open("../tree/tree"+ str(i) +".taxo", 'w')
    f.write(result)
    result = ""

print(dic_sp)
# Step 3, generate terms

result = ""
for item in dic_sp:
    result += dic_sp[item] + " \t " + item + "\n"
for i in range(4000):
    f = open("../term/tree" + str(i) + ".terms", 'w')
    f.write(result)
    f.close()