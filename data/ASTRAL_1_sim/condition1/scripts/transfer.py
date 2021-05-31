def transfer(file):
    f = open(file, 'r')
    result = ""
    pair = ""
    for line in f.readlines():
        if(line[0] == ">"):
            if(pair != ""):
                result += pair.replace("-", " \t ") + "\n"
                pair = ""
            pair += (line.replace("\n", "")).replace(">", "") + "-"
        else:
            pair += (line.replace("\n", ""))
    result += pair.replace("-", " \t ") + "\n"        
    f.close()
    return result

for i in range(4000):
    tmp = transfer("../alignment/original_data/" + str(i+1) + ".fasta")
    g = open("../alignment/tree" + str(i) + ".terms.embed", 'w')
    g.write(tmp)
    g.close()
