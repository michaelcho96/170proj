import networkx as nx
from utils import find_total_penalty
from utils import create_graph
from utils import add_solutions

def random_algorithm(input_graph):
	G = input_graph.copy()
	cycle_list = []
	pre_penalty = 0
	while G.nodes():
		try:
			edge_cycle = nx.find_cycle(G)
			vertex_cycle = []
			for edge in edge_cycle:
				vertex_cycle.append(edge[0])
				pre_penalty += G.node[edge[0]]['penalty']
				G.remove_node(edge[0])
			cycle_list.append(vertex_cycle)
		except:
			print("No cycle found")
			break	
	penalty = find_total_penalty(input_graph) - pre_penalty
	return [cycle_list, penalty]

def execute_random(index):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = random_algorithm(G)
	formatted_solution = [index, "Random", solution[1], solution[0]]
	list_solutions = [formatted_solution]
	add_solutions(list_solutions)

def run_on_all_instances():
	for instance in range(1,493):
		print("Processing input " + str(instance) + ".")
		execute_random(instance)

run_on_all_instances()
	