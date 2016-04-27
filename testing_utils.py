import networkx as nx 
from utils import find_cycles

def test_find_cycles1():
	G = nx.DiGraph()
	G.add_node(0)
	G.add_node(1)
	G.add_node(2)
	G.add_node(3)
	G.add_node(4)
	G.add_node(5)
	G.add_node(6)
	G.add_edge(1,2)
	G.add_edge(2,3)
	G.add_edge(3,1)
	G.add_edge(3,4)
	G.add_edge(4,5)
	G.add_edge(5,1)
	G.add_edge(1,0)
	G.add_edge(0,1)
	G.add_edge(5,0)
	G.add_edge(5,3)
	G.add_edge(1,6)
	list_cycles = find_cycles(G)
	for cycle in list_cycles:
		print(cycle)

def test_find_cycles2():
	G = nx.DiGraph()
	G.add_node(0)
	G.add_node(1)
	G.add_node(2)
	G.add_node(3)
	G.add_node(4)
	G.add_node(5)
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
	G.add_node(0)
	G.add_node(1)
	G.add_node(2)
	G.add_node(3)
	G.add_node(4)
	G.add_node(5)
	G.add_edge(0,1)
	G.add_edge(1,2)
	G.add_edge(2,0)
	G.add_edge(3,0)
	G.add_edge(0,3)
	G.add_edge(0,4)	
	list_cycles = find_cycles(G)
	for cycle in list_cycles:
		print(cycle)

test_find_cycles1()





