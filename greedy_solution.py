import networkx as nx
from utils import construct_cluster_graph
from utils import format_output_cycles
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions

def greedy_algorithm(G):
	CG = construct_cluster_graph(G)
	valid_nodes = CG.nodes()
	selected_nodes = []
	pre_penalty = 0
	while len(valid_nodes) != 0:
		node_selected = find_max_penalty(valid_nodes, CG)
		pre_penalty += CG.node[node_selected]['penalty']
		selected_nodes.append(node_selected)
		list_edges = CG.edges(node_selected, False)
		nodes_to_remove = set()
		for edge in list_edges:
			nodes_to_remove.add(edge[0])
			nodes_to_remove.add(edge[1])
		for node in nodes_to_remove:
			valid_nodes.remove(node)
	list_cycles = []
	for node in selected_nodes:
		cycle = []
		cycle.append(CG.node[node]['nodes'])
		list_cycles.append(cycle)
	penalty = find_total_penalty(G) - pre_penalty
	output_string = format_output_cycles(list_cycles)
	return [output_string, penalty]

	
def find_max_penalty(node_list, CG):
	max_penalty = 0
	max_node = None
	for node in node_list:
		penalty = CG.node[node]['penalty']
		if penalty > max_penalty:
			max_penalty = penalty
			max_node = node
	return max_node

list_solutions = []
for index in range(7,8):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = greedy_algorithm(G)
	formatted_solution = [index, "greedy", solution[1], solution[0]]
	list_solutions.append(formatted_solution)
add_solutions(list_solutions)







