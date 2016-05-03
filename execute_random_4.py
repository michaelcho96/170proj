from random_algorithm_4 import random_algorithm_4
from utils import create_graph
from utils import add_solutions
from utils import condensed_list
from utils import write_zero_penalty_list
from utils import combine
from utils import do_not_test_set
import sys
import os.path

def execute_random4(index, write_file):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = random_algorithm_4(G)
	formatted_solution = [index, "Random4", solution[1], solution[0]]
	list_solutions = [formatted_solution,]
	add_solutions(list_solutions, write_file)

def run_on_all_instances(write_file):
	filename = "COMBINED SOLUTIONS"

	for instance in range(1,493):
		if instance not in do_not_test_set(filename):
			print("Processing input " + str(instance) + ".")
			execute_random4(instance, write_file)
			execute_random4(instance, write_file)
			execute_random4(instance, write_file)

if len(sys.argv) != 2:
	print("Usage: execute_random_4.py write_file_name")
else:
	filename = sys.argv[1]
	run_on_all_instances(filename)	
