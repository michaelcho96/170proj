import networkx as nx
from utils import format_output_cycles
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions
from utils import contain_same_element
import multiprocessing
import time
import sys

solved_instance_list = [1, 3, 5, 6, 9, 10, 21, 23, 25, 27, 28, 30, 31, 32, 33, 36, 41, 42, 43, 44, 52,
                        53, 55, 64, 67, 72, 75, 77, 78, 80, 82, 83, 86, 89, 92, 95, 96, 97, 98, 99, 100,
                        101, 112, 115, 116, 119, 121, 133, 134, 135, 136, 138, 142, 145, 150, 152, 162, 163,
                        173, 174, 177, 179, 181, 183, 186, 188, 190, 191, 192, 194, 199, 202, 210, 214, 219,
                        223, 229, 231, 233, 239, 242, 245, 247, 250, 251, 254, 265, 267, 268, 269, 272, 274,
                        275, 276, 278, 280, 282, 290, 291, 292, 294, 295, 296, 298, 300, 305, 309, 313, 320,
                        323, 324, 326, 327, 328, 332, 336, 337, 338, 341, 342, 343, 350, 355, 356, 362, 364,
                        374, 375, 376, 379, 384, 385, 388, 390, 394, 395, 396, 397, 398, 402, 407, 410, 415,
                        421, 423, 425, 428, 441, 442, 443, 444, 447, 450, 452, 457, 458, 461, 463, 466, 471,
                        473, 475, 477, 478, 480, 481, 484, 488, 492]

def greedy_algorithm(G):
	CG = construct_cluster_graph(G)
	CG_copy = CG.copy()
	print "done constructing"
	valid_nodes = CG.nodes()
	selected_clusters = []
	pre_penalty = 0
	while len(valid_nodes) != 0:
		node_selected = find_min_weighted_degree(valid_nodes, CG)
		pre_penalty += CG.node[node_selected]['penalty']
		selected_clusters.append(node_selected)
		list_edges = CG.edges(node_selected, False)
		nodes_to_remove = set()
		nodes_to_remove.add(node_selected)
		for edge in list_edges:
			nodes_to_remove.add(edge[0])
			nodes_to_remove.add(edge[1])
		for node in nodes_to_remove:
			valid_nodes.remove(node)
			CG.remove_node(node)
	list_cycles = []
	for cluster in selected_clusters:
		list_cycles.append(CG_copy.node[cluster]['nodes'])
	penalty = find_total_penalty(G) - pre_penalty
	output_string = format_output_cycles(list_cycles)
	print(find_total_penalty(G), pre_penalty)
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

def find_min_weighted_degree(node_list, CG):
	min_weighted_degree = sys.maxsize
	selected_node = None
	for node in node_list:
		penalty = CG.node[node]['penalty']
		neighbor_penalty = 0
		list_edges = CG.edges(node, False)
		neighbors = set()
		for edge in list_edges:
			if edge[0] is not node:
				neighbors.add(edge[0])
			if edge[1] is not node:
				neighbors.add(edge[1])
		for n in neighbors:
			neighbor_penalty += CG.node[n]['penalty']
		weighted_degree = neighbor_penalty/penalty
		if weighted_degree < min_weighted_degree:
			min_weighted_degree = weighted_degree
			selected_node = node
	return selected_node

def execute_greedy(index):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = greedy_algorithm(G)
	formatted_solution = [index, "Greedy", solution[1], solution[0]]
	list_solutions = [formatted_solution]
	outfile = "SOLUTION RECORDS TONY"
	add_solutions(list_solutions, outfile)

# """ Constructs an undirected graph of all valid cycles, with an edge between two nodes
#    of the graph if the underlying cycles share at least one vertex """
# def construct_cluster_graph(G):
#     list_cycles = list(get_approx_cycles(G))
#     # We build our secondary graph of cycles
#     CGraph = nx.Graph()
#     counter = 0
#     for cycle in list_cycles:
#         penalty = 0
#         for node in cycle:
#             penalty += G.node[node]['penalty']
#         CGraph.add_node(counter, penalty= penalty, nodes=cycle)
#         counter += 1
#     # If two clusters contain the same node, then we draw 
#     # an edge between them.
#     for cluster_a in CGraph:
#         cluster_a_nodes = CGraph.node[cluster_a]['nodes']
#         for cluster_b in CGraph:
#             if cluster_a != cluster_b:
#                 cluster_b_nodes = CGraph.node[cluster_b]['nodes']
#                 if contain_same_element(cluster_a_nodes, cluster_b_nodes):
#                     CGraph.add_edge(cluster_a, cluster_b)
#     return CGraph

def construct_cluster_graph(input_graph):
	# find cycles through approximation
	G = input_graph.copy()
	CGraph = nx.Graph()
	counter = 0
	while G.nodes():
		source_node = G.nodes()[0]
		cycle = find_cycle(G, source_node)
		if cycle != []:
			penalty = 0
			i = 0
			for node in cycle:
			    penalty += G.node[node]['penalty']
			    if i % 2 == 0:
			    	G.remove_node(node)
			    i += 1
			CGraph.add_node(counter, penalty= penalty, nodes=cycle)
			counter += 1
		else:
			G.remove_node(source_node)
	print "done finding cycles"
	# If two clusters contain the same node, then we draw 
    # an edge between them.
	for cluster_a in CGraph:
		cluster_a_nodes = CGraph.node[cluster_a]['nodes']
		for cluster_b in CGraph:
			if cluster_a != cluster_b:
				cluster_b_nodes = CGraph.node[cluster_b]['nodes']
				if contain_same_element(cluster_a_nodes, cluster_b_nodes):
					CGraph.add_edge(cluster_a, cluster_b)
	print "done edges"
	return CGraph

def find_cycle(G, source_node):
	list_edges = find_edges_to_node(G, source_node)
	for edge in list_edges:
		source = edge[1]
		target = edge[0]
		try:
			cycle = nx.shortest_path(G, source=source, target=target)
			if not len(cycle) > 5:
				return cycle
		except:
			pass
	return []


def find_edges_to_node(G, source_node):
	list_edges = []
	for edge in G.edges():
		source = edge[0]
		target = edge[1]
		if target == source_node:
			list_edges.append(edge)
	return list_edges


def timed_execution():
	if __name__ == '__main__':
    	# Start foo as a process
		for index in range(1,493):
			if index in solved_instance_list:
				continue
			print("Processing input " + str(index) + ".")
			p = multiprocessing.Process(target=execute_greedy, name="execute_greedy", args=(index,))	
			p.start()
 			# Wait 10 seconds for foo
			time.sleep(5)
			if p.is_alive():
				print("Process " + str(index) + " still running. Killing.")
				p.terminate()
				# Cleanup
				p.join()
			p.join()

timed_execution()




