import networkx as nx
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions
from utils import format_output_cycles
from random import shuffle
import random

""" We repeatedly find valid cycles within G, removing them from the
	graph until there are no more cycles. We use those cycles as our
	solution """

def random_algorithm_4(input_graph):
	G = input_graph.copy()
	cycle_list = []
	pre_penalty = 0
	random_result = build_randomized_graph(input_graph)
	randG = random_result[0]
	nodes_dict = random_result[1]
	while randG.nodes():
		source_node = randG.nodes()[0]
		cycle = find_random_length_cycle(randG, source_node)
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

def find_random_length_cycle(G, root_node):
	cycle = []
	list_edges = find_edges_to_node(G, root_node)
	for edge in list_edges:
		source = edge[1]
		target = edge[0]
		try:
			cycle = nx.shortest_path(G, source=source, target=target)
			if len(cycle) > 5:
				cycle = []
			elif len(cycle) == 5:
				return cycle
			# If the cycle has less than five edges, we try to increase the number of
			# edges in the cycle by removing a random edge
			elif len(cycle) < 5:
				copyG = G.copy()	
				change = random.randint(0,1)
				copy_cycle = list(cycle)
				while change:
					cycle = change_cycle(copyG, source, target)
				#If altering the graph return no cycle, we revert the cycle
				if not cycle:
					cycle = copy_cycle
				return cycle
		except:
			pass
	return cycle

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

def change_cycle(G, cycle, source, target):
	new_cycle = []
	rand_edge = 0
	if len(cycle) == 4:
		rand_edge = random.randint(0, 2)
	elif len(cycle) == 3:
		rand_edge = random.randint(0, 1)
	edge_to_remove = (rand_edge, rand_edge + 1)
	G.remove_edge(edge_to_remove)
	try:
		new_cycle = nx.shortest_path(G, source=source, target=target)
	except:
		pass
	return new_cycle











