import networkx as nx

def create_graph(instance):
    """
    INSTANCE: File name containing instance of problem
    Parses file, returns a networkx Digraph object
    Nodes have 'penalty' attributes: 1 for adults, 2 for children.
    """
    with open(instance) as f:
        n = int(f.readline())
        children = f.readline().split(" ")
        g = nx.DiGraph()
        g.add_nodes_from([0,n], penalty=1)
        for c in children:
            if type(c) == int:
                g.node[c]['penalty'] = 2
            elif type(c) == str:
                g.node[int(c)]['penalty'] = 2
        for i in range(n):
            row = f.readline()
            elements = row.split(" ")
            for j in range(n):
                if elements[j] == 1:
                    g.add_edge(i,j)
    return g