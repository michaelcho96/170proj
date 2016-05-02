from random_algorithm_2 import random_algorithm_2
from utils import create_graph
from utils import add_solutions
from utils import condensed_list
from utils import write_zero_penalty_list
from utils import combine

def execute_random2(index):
	"""
	Executes random_algorithm_2 and returns a formatted solution.
	*** NO LONGER WRITES TO SOLUTION FILE ***
	"""
	filename = "instances/" + str(index) + ".in"
	G = create_graph(filename)
	solution = random_algorithm_2(G)
	formatted_solution = [index, "Random", solution[1], solution[0]]
	return formatted_solution
	# list_solutions = [formatted_solution,]
	# add_solutions(list_solutions)

def run_on_all_instances():
	for instance in range(1,493):
		if instance not in solved_instance_list:
			print("Processing input " + str(instance) + ".")
			for index in range (0,30):
				# execute_random2(instance)
				#^DOESNT WORK ANYMORE

def run_repeat():
	file_a = "UPDATED BEST RANDOM.txt"
	file_b = "SOLUTIONS RECORDS - M.txt"
	i = 0
	updated_instances = 0
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
					print("Processing input {0} on iteration {1}".format(str(instance), str(i)) + str(instance) + ".")
					min_penalty = 9999
					curr_best = None
					for index in range (0,30):
						print("{0}/30...".format(str(index + 1)))
						form_sol = execute_random2(instance)
						penalty = form_sol[1] 
						if penalty < curr_best:
							min_penalty = penalty
							curr_best = form_sol
							if min_penalty == 0:
								break
					add_solutions(file_b, [curr_best,])
			print("Updating {0} with {1}...".format(file_a, file_b))
			updated_instances += update_sol(file_a, file_b)
			print("Updating condensed solutions...")
			write_condensed_solutions(file_a)
	except KeyboardInterrupt:
		print("Repetition interrupted on instance {0} of iteration {1}. ".format(instance, i))


run_repeat()

