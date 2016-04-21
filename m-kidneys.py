import networkx as nx



def create_graph(instance):
    with open(instance_file) as f:
        n = f.readline()
        children = f.readline()
        g = nx.DiGraph()
        g.add_nodes_from([0,n])
        for i in range(n):
            row = f.readline()
            elements = row.split(" ")
            for j in range(n):
                if elements[j] == 1:
                    g.add_edge(i,j)
    return g


