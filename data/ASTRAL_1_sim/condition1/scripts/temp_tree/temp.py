alignment = {}
dic_letter = {"1": "A", "2": "C", "3": "T", "4": "G"}


def tackle(L):
    strr = ""
    for char in L:
        strr += dic_letter[char]
    return strr


for i in range(4000):
    f_alignment = open("../alignment/tree" +
                       str(i)+".terms.embed", "r")
    f_tree = open("../tree/tree"+str(i)+".taxo", "r")
    alignment = {}
    for line in f_alignment.readlines():
        if(len(line.split()) > 2):
            alignment[(line.split())[0]] = tackle((line.split())[1:])
    result_strr = str(len(alignment)) + "\n"
    for line in f_tree.readlines():
        check = line.split()
        if(check[0] in alignment):
            check[0] = alignment[check[0]]
        if(check[1] in alignment):
            check[1] = alignment[check[1]]
        result_strr += check[0] + "->" + check[1] + "\n"
        result_strr += check[1] + "->" + check[0] + "\n"
    f_alignment.close()
    f_tree.close()
    f = open("./temp" + str(i) + ".txt", 'w')
    f.write(result_strr)
    f.close()
