from random_algorithm_4 import random_algorithm_4
from utils import create_graph
from utils import add_solutions
from utils import condensed_list
from utils import write_zero_penalty_list
from utils import combine

def execute_random4(index):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = random_algorithm_2(G)
	formatted_solution = [index, "Random4", solution[1], solution[0]]
	list_solutions = [formatted_solution,]
	add_solutions(list_solutions, "greedy4_solutions")

def run_on_all_instances():
	for instance in range(1,493):
		if instance not in solved_instance_list:
			print("Processing input " + str(instance) + ".")
			execute_random2(instance)

