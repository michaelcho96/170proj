import sys
import networkx as nx


# def naive_sol(g, cycles):
#     """
#     In progress
#     """
#     new_cycles = nx.simple_cycles(g)
#     if len(all_cycles) == 0:
#         cost = 0
#         for node in nodes(g):
#             cost += get_node_attibutes(g, node)
#         return cost, cycles
#     short_cycles = []
#     for cycle in new_cycles:
#         if len(cycle) <= 5:
#             short_cycles.append(cycle)
#     for cycle in short_cycles:
#         sols = dict()
#         g_copy = g.copy()
#         for node in cycle:
#             g_copy.remove_node(node)
#         sols.add(g, naive_sol(g_copy, cycles.append(cycle)))
#     return min(sols, key=sols.get)

def create_graph(instance):
    """
    INSTANCE: File name containing instance of problem
    Parses file, returns a networkx Digraph object
    Nodes have 'penalty' attributes: 1 for adults, 2 for children.
    """
    print("creating graph of " + instance)
    with open(instance) as f:
        n = int(f.readline())
        print("n is " + str(n))
        children_line = f.readline()
        if children_line != "\n":
            children = children_line.split(" ")
            print(len(children))
            print(children)
        else: 
            children = []
        g = nx.DiGraph()
        g.add_nodes_from(range(n), penalty=1)
        for c in children:
            if type(c) == int:
                g.node[c]['penalty'] = 2
            elif type(c) == str:
                g.node[int(c.strip())]['penalty'] = 2
        for i in range(n):
            # print("i = " + str(i))
            row = f.readline()
            elements = row.split(" ")
            for j in range(n):
                if elements[j] == "1":
                    # print("adding edge " + str(j))
                    g.add_edge(i,j)
    print("nodes in g: " + str(len(nx.nodes(g))))
    print("edges in g: " + str(len(nx.edges(g))))
    return g

def naive_sol(g, cycles, sols):
    """
    In progress
    """
    print("running with {0} nodes".format(str(len(nx.nodes(g)))))
    new_cycles = list(nx.simple_cycles(g))
    # print("num cycles: " + str(len(new_cycles)))
    short_cycles = []
    for cycle in new_cycles:
        # print(cycle)
        if len(cycle) <= 6:
            short_cycles.append(cycle)
    if len(short_cycles) == 0:
        total_cost = 0
        costs = nx.get_node_attributes(g, "penalty")
        for node in nx.nodes(g):
            total_cost += costs[node]
        return total_cost, cycles
    # print("short cycles: " + str(len(short_cycles)))
    curr_min_cost = sys.maxsize
    curr_best_cycles = []
    for cycle in short_cycles:
        sols = dict()
        g_copy = g.copy()
        for node in cycle:
            g_copy.remove_node(node)
        cycles.append(cycle)
        copy_cost, copy_cycles_used = naive_sol(g_copy, cycles)
        if copy_cost < curr_min_cost:
            curr_min_cost = copy_cost
            curr_best_cycles = copy_cycles_used
    return curr_min_cost, curr_best_cycles, sols.add()


g = create_graph("TMDW3.in")
print(naive_sol(g, []))



