import networkx as nx
def find_cycles(input_graph):
	nodes = input_graph.nodes();
	visited = []
	for node in nodes:
		visited[node] = False
	visited[0] = True

def explore(root_node, node, input_graph, cycle):
	# At each vertex, we check to see if any of the edges lead back to the root
	# node. If so, we add that cycle to our list of cylces. If there are edges
	# which do not lead back to the vertex, we explore those nodes as well. 
	# Once we have searched all other edges, we return the list of cycles.

	#If the cycle has five elements in it, it can no longer qualify
	if (len(cycle) == 5):
		return [] 
	cycle_list = []
	for edge in input_graph.edges(node, False):
		next_vertex = edge[1]
		if edge[1] = root_node:
			cycle_list.append(cycle)
		else:
			updated_cycle = cycle
			updated_cycle.append[next_vertex]
			cycle_list.extend(explore(root_node, next_vertex, input_graph, updated_cycle))
		return cycle_list 
