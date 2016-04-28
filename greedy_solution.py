import networkx as nx
from utils import construct_cluster_graph

def greedy_alogrithm(G):
	CG = construct_cluster_graph(G)
	valid_nodes = CG.nodes()
	selected_nodes = []
	while not valid_nodes:
		node_selected = find_max_penalty(valid_nodes, CG)
		selected_nodes.append(node_selected)
		list_edges = CG.edges(node, False)
		for edge in list_edges:
			node_to_remove = edge[1]
			valid_nodes.remove(node_to_remove)
	list_cycles = []
	for node in selected_nodes:
		list_cycles.append(CG.node[node]['nodes'])
	return list_cycles

	
def find_max_penalty(node_list, CG):
	max_penalty = 0
	max_node = None
	for node in node_list:
		penalty = CG.node[node]['penalty']
		if penalty > max_penalty:
			max_penalty = penalty
			max_node = node
