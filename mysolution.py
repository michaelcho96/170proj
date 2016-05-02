import networkx as nx
from utils import construct_cluster_graph
from utils import format_output_cycles
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions

def algorithm(graph):
    CG = construct_cluster_graph(graph)
    valid_nodes = CG.nodes()
    adults = []
    start = valid_nodes.pop()
    selected_nodes = [start]
    pre_penalty = 0
    cycles = []
    current_cycle = []
    while selected_nodes != []:
        node = selected_nodes.pop(0)
        edges = CG.edges(node, False)
        if node in current_cycle:
            cycles.append(current_cycle)
            for n in current_cycle:
                pre_penalty += n['penalty']
                valid_nodes.remove(n)
            current_cycle = []
        current_cycle.append(node)
        for inner, outer in edges:
            neighbor = CG.node[outer]
            child_cycles = []
            if neighbor['penalty'] == 2:
                child_cycles.append(neighbor)
                selected_nodes.append(neighbor)
            else:
                adults.append(neighbor)
        if child_cycles == []:
            for adult in adults:
                selected_nodes.append(adult)
        child_cycles = []
        adults = []
    penalty = find_total_penalty(G) - pre_penalty
    output_string = format_output_cycles(cycles)
    return [output_string, penalty]


def execute(index):
    filename = "instances/" + str(index) + ".in"
    G = create_graph(filename)
    solution = algorithm(G)
    formatted_solution = [index, "Random", solution[1], solution[0]]
    print(solution[0])
    list_solutions = [formatted_solution,]
    add_solutions(list_solutions)

def run_on_all_instances():
    for instance in range(1,493):
        print("Processing input " + str(instance) + ".")
        execute(instance)

run_on_all_instances()







