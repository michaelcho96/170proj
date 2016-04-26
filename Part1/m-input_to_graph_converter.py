# import networkx as nx

# def create_graph(instance):
#     """
#     INSTANCE: File name containing instance of problem
#     Parses file, returns a networkx Digraph object
#     Nodes have 'penalty' attributes: 1 for adults, 2 for children.
#     """
#     with open(instance) as f:
#         n = int(f.readline())
#         children = f.readline().split(" ")
#         g = nx.DiGraph()
#         g.add_nodes_from([0,n], penalty=1)
#         for c in children:
#             if type(c) == int:
#                 g.node[c]['penalty'] = 2
#             elif type(c) == str:
#                 g.node[int(c)]['penalty'] = 2
#         for i in range(n):
#             row = f.readline()
#             elements = row.split(" ")
#             for j in range(n):
#                 if elements[j] == 1:
#                     g.add_edge(i,j)
#     return g

def naive_sol(g, cycles):
    """
    In progress
    """
    all_cycles = nx.simple_cycles(g)
    if len(all_cycles) == 0:
        cost = 0
        for node in nodes(g):
            cost += get_node_attibutes(g, node)
        return cost, cycles
    short_cycles = []
    for cycle in all_cycles:
        if len(cycle) <= 5:
            short_cycles.append(cycle)
    for cycle in short_cycles:
        sols = dict()
        g_copy = g.copy()
        for node in cycle:
            g_copy.remove_node(node)
        sols.add(naive_sol(cycles))

def graph_printer(input_graph):
    list_nodes = input_graph.nodes()
    list_edges = input_graph.list_edges()

def test_creation():
    output_graph = create_graph("SAMPLEINSTANCE.in")
    print("Construction complete.\n")
    print("List of nodes:\n")
    print(list_nodes, sep='\t')
    print("list of edges:\n")
    print(list_edges, sep='\t')
    print("Done!")
# Testing
test_creation()

