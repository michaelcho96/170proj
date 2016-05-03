from utils import combine
from utils import write_condensed_solutions
from utils import create_graph
from utils import do_not_test_set

#file_a = "CURRENT BEST SOLUTIONS"
#file_b = "SOLUTION_RECORDS_TONY.txt"
#combine(file_a, file_b)
#write_condensed_solutions("COMBINED SOLUTIONS")
"""G = create_graph("instances/12.in")
contains = False
edge_to_check = (119, 57)
for edge in G.edges():
	if edge_to_check == edge:
		contains = True
print(contains) """
optimal_sol_list = do_not_test_set("COMBINED SOLUTIONS")
out_file = open("Sub-Optimal Instances", "w")
read_file = open("Condensed Solution Records", "r")
read_data = read_file.readlines()
for element in range(1, 493):
	if element not in optimal_sol_list:
		line_data = read_data[element - 1]
		pre_penalty = line_data.split(":")
		penalty = pre_penalty[1].strip()
		out_file.write(str(element) + ": " + penalty + "\n")