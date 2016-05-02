from random_algorithm_2 import random_algorithm_2
from utils import create_graph
from utils import add_solutions
from utils import condensed_list
from utils import write_zero_penalty_list
from utils import combine

def execute_random2(index):
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = random_algorithm_2(G)
	formatted_solution = [index, "Random", solution[1], solution[0]]
	list_solutions = [formatted_solution,]
	add_solutions(list_solutions)

def run_on_all_instances():
	for instance in range(1,493):
		if instance not in solved_instance_list:
			print("Processing input " + str(instance) + ".")
			for index in range (0,30):
				execute_random2(instance)

def run_repeat():
	file_a = "UPDATED BEST RANDOM.txt"
	file_b = "SOLUTIONS RECORDS - M.txt"
	i = 0
	try:
		while True:
			i+= 1
			print("Starting iteration {0}.".format(str(i)))
			print("Getting solved instances...")
			solved = write_zero_penalty_list(file_a)
			print("{0} instances with penalty 0!".format(str(len(solved))))
			for instance in range(1, 493):
				if instance not in solved_instance_list:
					print("Processing input " + str(instance) + ".")
					for index in range (0,30):
						execute_random2(instance)
			print("Combining {0} and {1}...".format(file_a, file_b))
			combine(file_a, file_b)
			print("Updating condensed solutions...")
			write_condensed_solutions(file_a)
	except KeyboardInterrupt:
		print("Repetition interrupted on instance {0} of iteration {1}.".format(instance, i))

