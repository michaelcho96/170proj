import networkx as nx

def create_graph(instance):
    with open(instance) as f:
        n = int(f.readline())
        children = f.readline().split(" ")
        g = nx.DiGraph()
        g.add_nodes_from([0,n], child=False)
        for c in children:
            if type(c) == int:
                g.node[c]['child'] = True
            elif type(c) == str:
                g.node[int(c)]['child'] = True
            else:
                print("WTF")
        for i in range(n):
            row = f.readline()
            elements = row.split(" ")
            for j in range(n):
                if elements[j] == 1:
                    g.add_edge(i,j)
    return g


