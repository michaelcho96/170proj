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

# @timeout()
def naive_sol(g, cycles, all_cycles):
    """
    In progress
    """
    # print("running with {0} nodes and {1} cycles".format(str(len(nx.nodes(g))), len(cycles)))
    if len(all_cycles) == 0:
        total_cost = 0
        costs = nx.get_node_attributes(g, "penalty")
        for node in nx.nodes(g):
            total_cost += costs[node]
        # print("finishing with cost {0} and cycles {1}".format(total_cost, cycles))
        return total_cost, cycles
    curr_min_cost = sys.maxsize
    curr_best_cycles = []
    for cycle in all_cycles:
        all_cycles.remove(cycle)
        use_cycle = True
        for node in cycle:
            if node not in nx.nodes(g):
                use_cycle = False
        if use_cycle:
            g_copy = g.copy()
            for node in cycle:
                g_copy.remove_node(node)
            cycles_copy = cycles[:]
            cycles_copy.append(cycle)
            copy_cost, copy_cycles_used = naive_sol(g_copy, cycles_copy, all_cycles)
            if copy_cost < curr_min_cost:
                curr_min_cost = copy_cost
                curr_best_cycles = copy_cycles_used
    return curr_min_cost, curr_best_cycles

@timeout(15)
def all_short_cycles(g):
    all_cycles = nx.simple_cycles(g)
    short_cycles = []
    for cycle in all_cycles:
        if len(cycle) <= 5:
            short_cycles.append(cycle)
    return short_cycles

# def find_all_sol(outfile):
#     with open(outfile, 'w') as outf:
#         for i in range(1,493):
#             g = create_graph("instances/{0}.in".format(str(i)))
#             num_edges = len(nx.edges(g))
#             print("Graph has {0} edges...".format(str(num_edges)))
#             write_str = "None"
#             if len(nx.edges(g)) < 1000:
#                 print("Finding short cycles...")
#                 try:
#                     all_cycles = all_short_cycles(g)
#                     print("Running algorithm...")
#                     cost, cycles = naive_sol(g, [], all_cycles)
#                     if cycles == []:
#                         write_str = "{0}       None".format(str(cost))
#                     else: 
#                         write_str = "{0}       {1}".format(str(cost), format_output_cycles(cycles))
#                 except(TimeoutError):
#                     print("Timeout!")
#             else:
#                 print("Skipping!")
#             print(write_str)
#             print("\n")
#             outf.write(write_str + "\n")


def find_all_sol(outfile):
    with open(outfile, 'w') as outf:
            for i in range(1,493):
                sol = single_sol(i)

def single_sol(inst_num):
    if type(inst_num) is int:
        num = str(inst_num)
    elif type(inst_num) is str:
        num = inst_num
    else:
        raise TypeError
    print("Creating graph of instance {0}".format(num))
    g = create_graph("instances/{0}.in".format(num))
    num_edges = len(nx.edges(g))
    print("Graph has {0} edges...".format(str(num_edges)))
    write_str = "None"
    if len(nx.edges(g)) < 1000:
        print("Finding short cycles...")
        try:
            all_cycles = all_short_cycles(g)
            print("Running algorithm...")
            cost, cycles = naive_sol(g, [], all_cycles)
            if cycles == []:
                write_str = "{0}       None".format(str(cost))
            else: 
                write_str = "{0}       {1}".format(str(cost), format_output_cycles(cycles))
        except(TimeoutError):
            print("Timeout!")
    else:
        print("Skipping!")
    print(write_str + "\n")
    outf.write(write_str + "\n")
    return write_str

find_all_sol("m_all_out.txt")

# single_sol(71)
