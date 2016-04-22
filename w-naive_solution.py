import networkx as nx

# Finds a proper set of donation cycles
def find_donation_chain(input_digraph):
	cycles = input_digraph.simple_cycles()
	# If a cycle has more than 5 vertices, it is not valid.
	for cycle in cycles:
		if len(cycle) > 5:
			cycles.remove(cycle)
	# Remove cycles that share the same vertices
	cycles_to_remove = []
	vertices_used = []
	for cycle in cycles:
		if contains_used_node(cycle_a, vertices_used):
			cycles.remove(cycle)
		else:
			vertices_used.extend(cycle)
	return cycles


# Checks if a cycle contains a used node.
def contains_used_node(cycle, vertices_used):
	for node_a in cycle:
		for node_b in vertices_used:
			if node_a == node_b:
				return True
	return False

def find_cost(cycles, input_digraph):
	patients_treated = []
	for cycle in cycles:
		for vertex in cycle:
			patients_treated.append(vertex)
	return len(input_digraph.nodes()) - len(patients_treated)