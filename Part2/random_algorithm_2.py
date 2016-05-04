import networkx as nx
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions
from utils import format_output_cycles
from random import shuffle

""" We repeatedly find valid cycles within G, removing them from the
	graph until there are no more cycles. We use those cycles as our
	solution """

def random_algorithm_2(input_graph):
	G = input_graph.copy()
	cycle_list = []
	pre_penalty = 0
	random_result = build_randomized_graph(input_graph)
	randG = random_result[0]
	nodes_dict = random_result[1]
	while randG.nodes():
		source_node = randG.nodes()[0]
		cycle = find_cycle(randG, source_node)
		if cycle == []:
			randG.remove_node(source_node)
		else:
			real_cycle = []
			for node in cycle:
				real_cycle.append(nodes_dict[node])
			cycle_list.append(real_cycle)
			for node in cycle:
				real_node = nodes_dict[node]
				pre_penalty += G.node[real_node]['penalty']
				randG.remove_node(node)
	penalty = find_total_penalty(input_graph) - pre_penalty
	formatted_cycle_list = format_output_cycles(cycle_list)
	return [formatted_cycle_list, penalty]

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

""" Creates a dictionary which maps randomized nodes(int) to originalnode(int).
	The key is the shuffled node, the value is the original node. """
def randomize_graph(G):
	node_list = G.nodes()
	shuffled_node_list = list(node_list)
	shuffle(shuffled_node_list)
	node_dict = {}
	orginal_dict = {}
	for index in range(0, len(node_list)):
		node_dict[shuffled_node_list[index]] = node_list[index]
	for index in range(0, len(node_list)):
		orginal_dict[node_list[index]] = shuffled_node_list[index]
	return [node_dict, orginal_dict]

def build_randomized_graph(input_graph):
	dictionaries = randomize_graph(input_graph)
	original_dict = dictionaries[1]
	G = nx.DiGraph()
	for key in original_dict.keys():
		G.add_node(original_dict[key])
	for key in original_dict.keys():
		for edge in input_graph.edges(key, False):
			G.add_edge(original_dict[edge[0]], original_dict[edge[1]])
	return [G, dictionaries[0]]

