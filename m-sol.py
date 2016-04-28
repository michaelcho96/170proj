import sys
from utils import *
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

@timeout()
def naive_sol(g, cycles):
    """
    In progress
    """
    print("running with {0} nodes and {1} cycles".format(str(len(nx.nodes(g))), len(cycles)))
    new_cycles = list(nx.simple_cycles(g))
    short_cycles = []
    for cycle in new_cycles:
        if len(cycle) <= 5:
            short_cycles.append(cycle)
    if len(short_cycles) == 0:
        total_cost = 0
        costs = nx.get_node_attributes(g, "penalty")
        for node in nx.nodes(g):
            total_cost += costs[node]
        print("finishing with cost {0} and cycles {1}".format(total_cost, cycles))
        return total_cost, cycles
    # print("short cycles: " + str(len(short_cycles)))
    curr_min_cost = sys.maxsize
    curr_best_cycles = []
    for cycle in short_cycles:
        g_copy = g.copy()
        for node in cycle:
            g_copy.remove_node(node)
        cycles_copy = cycles[:]
        cycles_copy.append(cycle)
        copy_cost, copy_cycles_used = naive_sol(g_copy, cycles_copy)
        if copy_cost < curr_min_cost:
            curr_min_cost = copy_cost
            curr_best_cycles = copy_cycles_used
    return curr_min_cost, curr_best_cycles


g = create_graph("instances/225.in")
print(naive_sol(g, []))



