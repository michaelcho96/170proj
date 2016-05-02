import networkx as nx
from functools import wraps
import errno
import os
import signal
from shutil import copyfile
from best_solutions import write_file
from collections import defaultdict

# solved_instance_list = [1, 3, 5, 6, 9, 10, 21, 23, 25, 27, 28, 30, 31, 32, 33, 36, 41, 42, 43, 44, 52,
#                         53, 55, 64, 67, 72, 75, 77, 78, 80, 82, 83, 86, 89, 92, 95, 96, 97, 98, 99, 100,
#                         101, 112, 115, 116, 119, 121, 133, 134, 135, 136, 138, 142, 145, 150, 152, 162, 163,
#                         173, 174, 177, 179, 181, 183, 186, 188, 190, 191, 192, 194, 199, 202, 210, 214, 219,
#                         223, 229, 231, 233, 239, 242, 245, 247, 250, 251, 254, 265, 267, 268, 269, 272, 274,
#                         275, 276, 278, 280, 282, 290, 291, 292, 294, 295, 296, 298, 300, 305, 309, 313, 320,
#                         323, 324, 326, 327, 328, 332, 336, 337, 338, 341, 342, 343, 350, 355, 356, 362, 364,
#                         374, 375, 376, 379, 384, 385, 388, 390, 394, 395, 396, 397, 398, 402, 407, 410, 415,
#                         421, 423, 425, 428, 441, 442, 443, 444, 447, 450, 452, 457, 458, 461, 463, 466, 471,
#                         473, 475, 477, 478, 480, 481, 484, 488, 492]


""" INSTANCE: File name containing instance of problem
    Parses file, returns a networkx Digraph object
    Nodes have 'penalty' attributes: 1 for adults, 2 for children. """
def create_graph(instance):
    
    with open(instance) as f:
        n = int(f.readline())
        children_line = f.readline()
        if children_line != "\n":
            children = children_line.split()
            # print(children)
        else: 
            children = []
        g = nx.DiGraph()
        g.add_nodes_from(range(n), penalty=1)
        for c in children:
            if c == "\n" or c == " ":
                pass
            elif type(c) == int:
                g.node[c]['penalty'] = 2
            elif type(c) == str:
                g.node[int(c.strip())]['penalty'] = 2
        for i in range(n):
            row = f.readline()
            elements = row.split()
            # print(elements)
            for j in range(n):
                if "1" in elements[j]:
                    g.add_edge(i,j)
        # print("num edges: " + str(len(nx.edges(g))))
    return g

        
""" Constructs an undirected graph of all valid cycles, with an edge between two nodes
   of the graph if the underlying cycles share at least one vertex """
def construct_cluster_graph(G):
    list_cycles = list(nx.simple_cycles(G))
    # We build our secondary graph of cycles
    CGraph = nx.Graph()
    counter = 0
    for cycle in list_cycles:
        penalty = 0
        for node in cycle:
            penalty += G.node[node]['penalty']
        CGraph.add_node(counter, penalty= penalty, nodes=cycle)
        counter += 1
    # If two clusters contain the same node, then we draw 
    # an edge between them.
    for cluster_a in CGraph:
        cluster_a_nodes = CGraph.node[cluster_a]['nodes']
        for cluster_b in CGraph:
            if cluster_a != cluster_b:
                cluster_b_nodes = CGraph.node[cluster_b]['nodes']
                if contain_same_element(cluster_a_nodes, cluster_b_nodes):
                    CGraph.add_edge(cluster_a, cluster_b)
    return CGraph

""" Helper function for construct_cluster_graph() """
def contain_same_element(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False

"""Takes in a list of cycles and outputs a submittable format """
def format_output_cycles(cycle_list):
    output_string = ""
    for cycle in cycle_list:
        for node in cycle:
            output_string += str(node)
            output_string += " "
        output_string = output_string[0:len(output_string) - 1]
        output_string = output_string + "; "
    output_string = output_string[0:len(output_string) - 2]
    return output_string

def find_total_penalty(G):
    penalty = 0
    for node in G.nodes():
        penalty += G.node[node]['penalty']
    return penalty

def contains_edge(G, input_edge):
    for edge in G.edges():
        if edge == input_edge:
            return True
    return False



########################
## SOLUTION FUNCTIONS ##
########################
def combine(a, b):
    """
    usage ex:
    file_a = "SOLUTIONS RECORDS.txt"
    file_b = "SOLUTIONS RECORDS - M.txt"
    """
    out_f = open("COMBINED SOLUTIONS", "w")
    file_a = open(a, "r")
    file_b = open(b, "r")
    data_a = file_a.readlines()
    data_b = file_b.readlines()
    for index in range(0,492):
        line_a = read_solution_line(data_a[index])
        line_b = read_solution_line(data_b[index])
        if line_a[2] < line_b[2]:
            print("Updating solution for instance {0} from {1} to {2}".format(str(index + 1), line_b[2]))
            out_f.write(data_a[index])
        else:
            out_f.write(data_b[index])

def update_sol_list(base, new, log="log.txt"):
    """
    base = old file you want to be updated
    new = new instances to be checked against base
    """
    num_updated = 0
    with open(log, "r") as logf:
        with open("log.tmp", "w") as new_log:
            with open("new_best.tmp", "w") as out_f:
                with open(base, "r") as base_f:
                    with open(new, "r") as new_f:
                        data_a = base_f.readlines()
                        data_b = new_f.readlines()
                        log_lines = logf.readlines()
                        for i in range(0,492):
                            line_a = read_solution_line(data_a[i])
                            line_b = read_solution_line(data_b[i])
                            if line_a[2] < line_b[2]:
                                print("Updating solution for instance {0} from {1} to {2}".format(str(index + 1), line_b[2], line_a[2]))
                                new_logline = log_lines[i] + str(line_a[2])
                                new_log.write(new_logline)
                                out_f.write(data_a[i]) 
                                num_updated += 1
                            else:
                                out_f.write(data_b[i])
    copyfile("new_best.tmp", base)
    copyfile("log.tmp", log)
    return num_updated



def write_condensed_solutions(input_f):
    read_file = open(input_f, "r")
    out_file = open("Condensed Solution Records", "w")
    data = read_file.readlines()
    for line in data:
        penalty_tokens = line.split("|")
        instance_tokens = line.split(":")
        instance_number = instance_tokens[0]
        penalty = penalty_tokens[1]
        out_file.write(instance_number + ": " + penalty + "\n")

def write_zero_penalty_list(input_f):
    lst = []
    read_file = open(input_f, "r")
    out_file = open("Zero Penalty Instances", "w")
    data = read_file.readlines()
    for line in data:
        penalty_tokens = line.split("|")
        instance_tokens = line.split(":")
        instance_number = instance_tokens[0]
        penalty = penalty_tokens[1]
        if int(penalty) == 0:
            out_file.write(instance_number + ", ")
            lst.append(instance_number)
    return lst


def condensed_list(solved_instance_list):
    instance_list = []
    for index in range(1,493):
        if not index in solved_instance_list:
            instance_list.append(index)
    return instance_list

def read_solution_line(line):
    instance_tokens = line.split(":")
    type_tokens = line.split(",")
    tokens = line.split("|")
    #Finding instance number
    instance_number = int(instance_tokens[0])
    #FInding algorithm
    type_token2 = type_tokens[0].split(" ")
    algorithm_type = type_token2[1]
    #Finding penalty
    penalty = int(tokens[1])
    #Finding solution
    solution = tokens[2]
    solution = solution.replace('\n', "")
    solution = solution.replace('', "")
    return [instance_number, algorithm_type, penalty, solution]

def add_solutions(list_solutions, out_file="DEFAULT_OUT"):
    write_file(out_file, list_solutions)

def validate_formatted_solution(solution):
    cycle_list = []
    used_nodes = []
    cycle_tokens = solution.split(";")
    for node_tokens in cycle_tokens:
        cycle = []
        node_token = node_tokens.split(" ")
        for node in node_token:
            if node != '' and node != '\n':
                if int(node) in used_nodes:
                    print("repeat node")
                    return False
                cycle.append(int(node))
                used_nodes.append(int(node))
        if len(cycle) == 1:
            print("cycle of length 1")
            return False
        cycle_list.append(cycle)
    for cycle in cycle_list:
        if len(cycle) > 5:
            return False
    return True

def comprehensive_solution_validation(solution, G):
    if not validate_formatted_solution(solution):
        return False
    else:
        solution = solution.replace('\n', "")
        solution = solution.replace('', "")
        #print("solution: " + solution)
        list_cycles = solution.split(";")

        # Each token in tokens1 is a list of cycles
        for cycle in list_cycles:
            # each token in tokens2 is a node
            nodes = cycle.split(" ")
            list_nodes = []
            for node in nodes:
                if node != '' and node != '\n':
                    list_nodes.append(node)
            #print("list_nodes: " + str(list_nodes))
            for index in range(0, len(list_nodes)):
                edge_to_check = ()
                if index == len(list_nodes) - 1:
                    edge_to_check = (int(list_nodes[index]), int(list_nodes[0]))
                else:
                    edge_to_check = (int(list_nodes[index]), int(list_nodes[index + 1]))
                #print("Checking: " + str(edge_to_check))
                if not contains_edge(G, edge_to_check):
                 #   print("Contains edge not in graph.")
                    return False
    return True



########################
####### MISC ###########
########################
class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

 ########################
 ##### DEPRECATED #######
 ########################   
""" DO NOT USE: RUNTIME |V|^6 """
def find_cycles(input_graph):
    G = input_graph.copy()
    cycle_list = []
    list_nodes = G.nodes()
    for node in list_nodes:
        print("searching node " + str(node))
        cycle_list.extend(_explore2(node, node, G, [node]))
        G.remove_node(node)
    return cycle_list

def _explore(node, input_graph, counter):
    cycle_list = []
    node_previsit = counter
    G.node[node]['pre-visit'] = node_previsit
    counter += 1
    for edge in input_graph.edges(node, False):
        next_vertex = edge[1]
        if G.node[next_vertex]['pre-visit'] < node_previsit:
            # We explore for cycles
            # Place code here
            print("error: need code")
        cycles_list.extend(__explore(next_vertex))

def _explore2(root_node, node, input_graph, path):
    cycle_list = []
    if len(path) == 6: # If the path already has six vertices, then there is no valid cycle
        return cycle_list
    for edge in input_graph.edges(node, False):
        next_node = edge[1]
        if next_node == root_node:
            cycle_list.append(path)
        else:
            updated_path = list(path)
            updated_path.append(next_node)
            updated_graph = input_graph.copy()
            if node != root_node:
                updated_graph.remove_node(node)
            cycle_list.extend(_explore2(root_node, next_node, updated_graph, updated_path)) # Recursive call
    return cycle_list

