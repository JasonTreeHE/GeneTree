import dendropy
######################################################


def check_root(node):
    if(node.parent_node == None):
        return True
    return False


def rename_tree(T, prefix):
    i = 0
    for n in T.postorder_node_iter():
        if(n.taxon == None):
            n.taxon = dendropy.datamodel.taxonmodel.Taxon(
                label=prefix + str(i))
            i += 1


print(1)


def print_pair(tree):
    result = ""
    store = []
    for node in tree.postorder_node_iter():
        if (check_root(node) == False):
            if(check_root(node.parent_node) == False):  # The node's parent is not root
                result += (node.taxon.label + " \t " +
                           node.parent_node.taxon.label) + "\n"
            else:  # The node's parent is the root
                store.append(node)
    result += (store[0].taxon.label + " \t " + store[1].taxon.label) + "\n"
    return result


f = open("../tree/original_data/true-trees-1X", "r")

idx = 0
for line in f.readlines():
    temp = (line.replace("\n", ""))
    tree = dendropy.Tree.get(
        data="[&R] " + temp, schema="newick", rooting="force-rooted")
    rename_tree(tree, "t" + str(idx) + "_")
    g = open(("../tree/tree"+str(idx)+".taxo"), 'w')
    g.write(print_pair(tree))
    g.close()
    idx += 1
