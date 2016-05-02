from random_algorithm_2 import random_algorithm_2
from utils import create_graph
from utils import add_solutions

def execute_random2(index):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = random_algorithm_2(G)
	formatted_solution = [index, "Random", solution[1], solution[0]]
	list_solutions = [formatted_solution,]
	add_solutions(list_solutions)

def run_on_all_instances():
	for instance in range(1,493):
		print("Processing input " + str(instance) + ".")
		for index in range (0,20):
			execute_random2(instance)

run_on_all_instances()