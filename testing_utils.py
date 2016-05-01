import networkx as nx 
from utils import find_cycles
from utils import construct_cluster_graph
from utils import format_output_cycles
#from greedy_solution import greedy_algorithm
#from random_algorithm import random_algorithm
from utils import validate_formatted_solution
from random_algorithm_2 import random_algorithm_2
from utils import create_graph
from random import shuffle	
from random_algorithm_2 import build_randomized_graph
#from utils import simple_k_cycles

def test_find_cycles1():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5,6])
	G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1),(1,0),(0,1),(5,0),(5,3),(1,6)])
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

def test_simple_k_cycles():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5,6])
	G.add_edges_from[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0)]
	print("starting")
	cycles_list = list(simple_k_cycles(G, 5))
	print("done")
	for cycle in cycles_list:	
		print(cycle)

def test_random_algorithm():
	G= nx.Graph()
	G.add_nodes_from([0,1,2,3,4,5])
	G.add_edges_from([[0,1],[1,2],[2,0],[3,4],[4,5],[5,3]])
	for node in range(0,6):
		G.node[node]['penalty'] = 1
	cycles_list = random_algorithm(G)
	for cycle in cycles_list:
		print(cycle)

def test_validate_formatted_solution():
	solution = "1 2 3 4"
	print(validate_formatted_solution(solution))
	solution = "1 2; 3 4 5 6 7"
	print(validate_formatted_solution(solution))
	solution = "1 2; 3 4 5; 6 7 8 9 10 11"
	print(validate_formatted_solution(solution))
	solution = "1 2; 3 4 5; 5 6; 7"
	print(validate_formatted_solution(solution))
	solution = "1 2; 3 4 5; 8 6; 7"
	print(validate_formatted_solution(solution))	

def test_shortest_paths():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5])
	G.add_edges_from([[0,1],[1,2],[2,0],[3,4],[4,5],[5,3]])
	cycle = nx.shortest_path(G, source=0, target=2)
	for node in cycle:
		print(node)

def test_random_algorithm_2():
	G= nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5])
	G.add_edges_from([[0,1],[1,2],[2,0],[3,4],[4,5],[5,3]])
	for node in range(0,6):
		G.node[node]['penalty'] = 1
	solution = random_algorithm_2(G)
	print("Penalty: " + str(solution[1]))
	print("Cycles: " + solution[0])

def test_random_algorithm_2_2():
	G= nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5])
	G.add_edges_from([[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]])
	for node in range(0,6):
		G.node[node]['penalty'] = 1
	solution = random_algorithm_2(G)
	print("Penalty: " + str(solution[1]))
	print("Cycles: " + solution[0])

def test_random_algorithm_2_3():
	filename = "instances/2.in"
	G = create_graph(filename)
	solution = random_algorithm_2(G)
	print("Penalty: " + str(solution[1]))
	print("Cycles: " + solution[0])
	print(validate_formatted_solution(solution[0]))
	
def test_build_randomized_graph():
	G = nx.DiGraph()
	G.add_nodes_from([0,1,2,3,4,5])
	G.add_edges_from([[0,1],[1,2],[2,0],[3,4],[4,5],[5,3]])
	for node in range(0,6):
		G.node[node]['penalty'] = 1
	rand_G = build_randomized_graph(G)
	print(rand_G.nodes())
	print(rand_G.edges())	

def test_build_randomized_graph2():
	filename = "instances/2.in"
	G = create_graph(filename)
	rand_G = build_randomized_graph(G)
	print(rand_G.nodes())
	print(rand_G.edges())

#test_greedy_algorithm()
#test_construct_cluster_graph()
#test_simple_k_cycles()
#test_find_cycles3()
#test_random_algorithm()
#test_validate_formatted_solution()
#test_shortest_paths()
#test_random_algorithm_2_3()
test_build_randomized_graph()



