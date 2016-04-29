import sys
from utils import *
import networkx as nx
import datetime
from collections import defaultdict


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
    if len(all_cycles) == 0 or current_penalty == 0:
        # print("finishing with cost {0} and cycles {1}".format(current_penalty, cycles))
        return current_penalty, cycles
    # Calculate Total Penalty
    curr_min_penalty = current_penalty
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
            copy_penalty, copy_cycles_used = naive_sol(g_copy, cycles_copy, all_cycles_copy)
            if copy_penalty < curr_min_penalty:
                curr_min_penalty = copy_penalty
                curr_best_cycles = copy_cycles_used
                if curr_min_penalty == 0:
                    break
    return curr_min_penalty, curr_best_cycles

# @timeout(600)
def all_short_cycles(g):
    all_cycles = simple_k_cycles(g, 5)
    short_cycles = []
    for cycle in all_cycles:
        if len(cycle) <= 5:
            short_cycles.append(cycle)
        else:
            print("cycle thing didn't work...")
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

    for i in range(1,493):
        sol, log = single_sol(i)
        with open(outfile, 'a') as outf:
            outf.write(sol + "\n")
        # with open(logfile, 'a') as logf:
            # logf.write(log + "\n")


# @timeout()
def single_sol(inst):
    log_str = ""
    if type(inst) is int:
        num = str(inst)
        in_file = "instances/{0}.in".format(num)
        update = "Creating graph of instance {0}".format(num)
        print(update)
        log_str += update + "\n"
    elif type(inst) is str:
        in_file = inst
        update = "Creating graph of {0}".format(in_file)
        print(update)
        log_str += update + "\n"
    else:
        raise TypeError
    g = create_graph(in_file)
    num_edges = len(nx.edges(g))
    update = "Graph has {0} edges...".format(str(num_edges))
    print(update)
    log_str += update + "\n"
    write_str = "Skipped"
    if len(nx.edges(g)) < 10000000:
        update = "Finding short cycles..."
        print(update)
        log_str += update + "\n"
        try:
            all_cycles = all_short_cycles(g)
            print("We have {0} cycles...".format(len(all_cycles)))
            if len(all_cycles) > 20:
                print("Too many cycles :(")
                write_str = "too many cycles"
            else:
                update = "Running algorithm on {0} cycles...".format(len(all_cycles))
                print(update)
                log_str += update + "\n"
                cost, cycles = naive_sol(g, [], all_cycles)
                if cycles == []:
                    write_str = "{0}       None".format(str(cost))
                else: 
                    write_str = "{0}       {1}".format(str(cost), format_output_cycles(cycles))
        except(TimeoutError):
            update = "Timeout!"
            print(update)
            log_str += update + "\n"
    else: 
        update = "Skipping!"
        print(update)
        log_str += update    
    update = str(inst) + write_str + "\n"
    print(update + "\n")
    log_str += update + "\n"
    return write_str, log_str


# date_suffix = datetime.now()
find_all_sol("m_all_out3.txt")

def single_sol_by_input():
    inp = input("Enter instance number, or None: ")
    if inp != "None":
        single_sol(int(inp))

# single_sol_by_input()

# single_sol("part1/tmdw1.in")

def sol_by_range(start, end):
    if start not in range(0,493):
        raise ValueError("Start not in range")
    if end not in range(0,493):
        raise ValueError("End not in range")
    if start >= end:
        raise ValueError("Start must be before end")
    with open("m_out_{0}-{1}.txt".format(str(start), str(end)), "w") as outf:
        for i in range(start, end + 1):
            sol, log = single_sol(i)
            outf.write(sol + "\n")

# sol_by_range(1,10)
