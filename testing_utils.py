import networkx as nx 
from utils import find_cycles
from utils import construct_cluster_graph
from utils import format_output_cycles
from greedy_solution import greedy_algorithm

def test_find_cycles1():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5,6])
	G.add_nodes_from([(1,2),(2,3),(3,4),(4,5),(5,1),(1,0),(0,1),(5,0),(5,3),(1,6)])
	G.add_edge(1,6)
	list_cycles = find_cycles(G)
	for cycle in list_cycles:
		print(cycle)

def test_find_cycles2():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5])
	G.add_edge(0,1)
	G.add_edge(1,2)
	G.add_edge(2,3)
	G.add_edge(3,4)
	G.add_edge(4,5)
	G.add_edge(5,0)	
	list_cycles = find_cycles(G)
	for cycle in list_cycles:
		print(cycle)

def test_find_cycles3():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4])
	G.add_edge(0,1)
	G.add_edge(1,2)
	G.add_edge(2,0)
	G.add_edge(3,0)
	G.add_edge(0,3)
	G.add_edge(0,4)	
	list_cycles = find_cycles(G)
	for cycle in list_cycles:
		print(cycle)

def test_construct_cluster_graph():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5,6,7,8])
	G.add_edges_from([(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(2,5),(5,6),(6,2),(1,7),(7,8),(8,1)])
	for node in G.nodes():
		G.node[node]['penalty'] = 1
	CG = construct_cluster_graph(G)
	for cluster in CG.nodes():
		print("cluster number:" + str(cluster) + "\n" +
			  "cluster value:" + str(CG.node[cluster]['penalty']))
		print("cluster members: ")
		node_list = CG.node[cluster]['nodes']
		for node in node_list: 
			print(str(node))
	for edge in CG.edges():
		print(edge)

def test_format_output_cycles():
	output_list = [[0,1,2], [3,4,5], [6,7,8]]
	print(format_output_cycles(output_list))

def test_greedy_algorithm():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5,6,7,8])
	G.add_edges_from([(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(1,5),(5,6),(6,1),(2,7),(7,8),(8,2)])
	for node in range(0,4):
		G.node[node]['penalty'] = 2
	for node in range(4,9):
		G.node[node]['penalty'] = 1
	solution = greedy_algorithm(G)
	print("Penalty: " + str(solution[1]))
	print("Solution: " + solution[0])

test_greedy_algorithm()
#test_construct_cluster_graph()







