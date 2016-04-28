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
    all_nodes = nx.nodes(g)
    num_nodes = len(all_nodes)
    costs = nx.get_node_attributes(g, "penalty")
    current_penalty = 0
    for node in all_nodes:
        current_penalty += costs[node]
    # print("Current Penalty: {0}".format(current_penalty))
    # print("running with {0} nodes and {1} cycles".format(str(num_nodes), len(cycles)))
    if len(all_cycles) == 0 or num_nodes == 0:
        # print("finishing with cost {0} and cycles {1}".format(current_penalty, cycles))
        return current_penalty, cycles
    # Calculate Total Penalty
    curr_min_cost = current_penalty
    curr_best_cycles = cycles.copy()
    for cycle in all_cycles:
        all_cycles_copy = all_cycles.copy()
        all_cycles_copy.remove(cycle)
        use_cycle = True
        for node in cycle:
            if node not in nx.nodes(g):
                # print("not using cycle")
                use_cycle = False
        if use_cycle:
            g_copy = g.copy()
            for node in cycle:
                g_copy.remove_node(node)
            cycles_copy = cycles.copy()
            cycles_copy.append(cycle)
            copy_cost, copy_cycles_used = naive_sol(g_copy, cycles_copy, all_cycles_copy)
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
                outf.write(sol + "\n")

def single_sol(inst):
    if type(inst) is int:
        num = str(inst)
        in_file = "instances/{0}.in".format(num)
        print("Creating graph of instance {0}".format(num))
    elif type(inst) is str:
        in_file = inst
        print("Creating graph of {0}".format(in_file))
    else:
        raise TypeError
    g = create_graph(in_file)
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
    return write_str

# find_all_sol("m_all_out.txt")

single_sol("part1/tmdw2.in")
