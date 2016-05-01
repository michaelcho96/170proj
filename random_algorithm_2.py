import networkx as nx
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions
from utils import format_output_cycles

""" We repeatedly find valid cycles within G, removing them from the
	graph until there are no more cycles. We use those cycles as our
	solution """

def random_algorithm_2(input_graph):
	G = input_graph.copy()
	cycle_list = []
	pre_penalty = 0
	while G.nodes():
		cycle = find_cycle(G)
		cycle_list.append(cycle)
		for node in cycle:
			pre_penalty += G.node[node]['penalty']
			G.remove_node(node)
	penalty = find_total_penalty(input_graph) - pre_penalty
	formatted_cycle_list = format_output_cycles(cycle_list)
	return [formatted_cycle_list, penalty]

def find_cycle(G):
	# Uses first node as node
	node = G.nodes()[0]
	list_edges = find_edges_to_node(G, node)
	for edge in list_edges:
		source = edge[1]
		target = edge[0]
		try:
			cycle = nx.shortest_path(G, source=source, target=target)
			if not len(cycle) > 5:
				return cycle
		except:
			print("no cycle.")
	return []


def find_edges_to_node(G, source_node):
	list_edges = []
	for edge in G.edges():
		source = edge[0]
		target = edge[1]
		if target == source_node:
			list_edges.append(edge)
	return list_edges