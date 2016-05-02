from random_algorithm_2 import random_algorithm_2
from utils import create_graph
from utils import add_solutions
from utils import condensed_list
from utils import write_zero_penalty_list
from utils import combine
from utils import update_sol_list
from utils import *

def execute_random2(index, graphs):
	"""
	Executes random_algorithm_2 and returns a formatted solution.
	*** NO LONGER WRITES TO SOLUTION FILE ***
	"""
	filename = "instances/" + str(index) + ".in"
	if index not in graphs:
		G = create_graph(filename)
		graphs[index] = G
	else:
		G = graphs[index]
	solution = random_algorithm_2(G)
	formatted_solution = [index, "Random", solution[1], solution[0]]
	return formatted_solution, graphs
	# list_solutions = [formatted_solution,]
	# add_solutions(list_solutions)

def run_on_all_instances():
	for instance in range(1,493):
		if instance not in solved_instance_list:
			print("Processing input " + str(instance) + ".")
			for index in range (0,30):
				pass
				# execute_random2(instance)
				#^DOESNT WORK ANYMORE

def run_repeat_safe():
	file_a = "UPDATED BEST RANDOM.txt"
	file_b = "SOLUTIONS RECORDS - M.txt"
	i = 0
	updated_instances = 0
	graphs = {}
	try:
		while True:
			i+= 1
			print("Starting iteration {0}...".format(str(i)))
			print("Getting solved instances...")
			solved = write_zero_penalty_list(file_a)
			print(solved)
			print("{0} instances with penalty 0!".format(str(len(solved))))
			for instance in range(1, 493):
				if str(instance) not in solved:
					print("\nProcessing input {0} on iteration {1}".format(str(instance), str(i)))
					min_penalty = 9999
					curr_best = None
					for index in range (0,30):
						print(".", end="")
						form_sol, graphs = execute_random2(instance, graphs)
						penalty = form_sol[2] 
						if penalty < min_penalty:
							min_penalty = penalty
							curr_best = form_sol
							if min_penalty == 0:
								break
					add_solutions(file_b, [curr_best,])
			print("Updating {0} with {1}...".format(file_a, file_b))
			updated_instances += update_sol_list(file_a, file_b)
			print("Updating condensed solutions...")
			write_condensed_solutions(file_a)
	except KeyboardInterrupt:
		print("Repetition interrupted on instance {0} of iteration {1}. ".format(instance, i))

def run_repeat_fast():
	file_a = "UPDATED BEST RANDOM.txt"
	file_b = "SOLUTIONS RECORDS - M.txt"
	i = 0
	updated_instances = 0
	sol_list = []
	graphs = {}
	try:
		while True:
			i+= 1
			print("Starting iteration {0}...".format(str(i)))
			print("Getting solved instances...")
			solved = write_zero_penalty_list(file_a)
			print(solved)
			print("{0} instances with penalty 0!".format(str(len(solved))))
			for instance in range(1, 493):
				if str(instance) not in solved:
					print("\nProcessing input {0} on iteration {1}".format(str(instance), str(i)))
					min_penalty = 9999
					curr_best = None
					for index in range (0,30):
						print(".", end="")
						form_sol, graphs = execute_random2(instance, graphs)
						if instance == 12: 
							print("doing something")
						penalty = form_sol[2] 
						if penalty < min_penalty:
							min_penalty = penalty
							curr_best = form_sol
							if min_penalty == 0:
								print("\n Found a 0!")
								break
					sol_list.append(curr_best)
			print("Addng all solutions...")
			add_solutions(sol_list)
			print("Updating {0} with {1}...".format(file_a, file_b))
			updated_instances += update_sol_list(file_a, file_b)
			print("Updating condensed solutions...")
			write_condensed_solutions(file_a)
	except KeyboardInterrupt:
		print("Repetition interrupted on instance {0} of iteration {1}. ".format(instance, i))



run_repeat_fast()

