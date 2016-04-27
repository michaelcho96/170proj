import networkx as nx

def create_graph(instance):
    """
    INSTANCE: File name containing instance of problem
    Parses file, returns a networkx Digraph object
    Nodes have 'penalty' attributes: 1 for adults, 2 for children.
    """
    print("creating graph of " + instance)
    with open(instance) as f:
        n = int(f.readline())
        children_line = f.readline()
        if children_line != "\n":
            children = children_line.split(" ")
        else: 
            children = []
        g = nx.DiGraph()
        g.add_nodes_from(range(n), penalty=1)
        for c in children:
            if c == "\n":
                pass
            elif type(c) == int:
                g.node[c]['penalty'] = 2
            elif type(c) == str:
                g.node[int(c.strip())]['penalty'] = 2
        for i in range(n):
            row = f.readline()
            elements = row.split(" ")
            print(elements)
            for j in range(n):
                if "1" in elements[j]:
                    g.add_edge(i,j)
        print("num edges: " + str(len(nx.edges(g))))
    return g

def find_cycles(input_graph):
    nodes = input_graph.nodes();
    list_cycles = []
    for node in nodes:
        list_cycles.extend(explore(node, node, input_graph, []))
        input_graph.remove_node(node)
    return list_cycles

def explore(root_node, node, input_graph, cycle):
    # At each vertex, we check to see if any of the edges lead back to the root
    # node. If so, we add that cycle to our list of cylces. If there are edges
    # which do not lead back to the vertex, we explore those nodes as well. 
    # Once we have searched all other edges, we return the list of cycles.

    #If the cycle has five elements in it, it can no longer qualify
    cycle.append(node)
    cycle_list = []
    if (len(cycle) == 6):
        return cycle_list
    # We look at all edges from node, checking if a cycle is found.
    # print(input_graph.edges(node, False ))
    for edge in input_graph.edges(node, False):
        next_vertex = edge[1]
        if next_vertex == root_node:
            cycle_list.append(cycle)
        else:
            updated_cycle = list(cycle)
            updated_graph = input_graph.copy()
            if node != root_node:
                updated_graph.remove_node(node)
            cycle_list.extend(explore(root_node, next_vertex, updated_graph, updated_cycle))
    return cycle_list 







