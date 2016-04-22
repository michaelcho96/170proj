import networkx as nx

def make_graph(number_nodes):
	G = nx.Graph()
	for node in range(0, number_nodes):
		G.add_node(node)
	print("Number of nodes: %s" %(G.number_of_nodes()))
make_graph(4)
