import os.path
import io
from shutil import copyfile

""" STORES THE BEST SOLUTIONS """
""" HOW TO USE: You should input a list of solutions. Each 
	solution should be in this form: [instance number, algorithm_name, penalty, new_solution ].
	The instance_number should be an INT, algorithm_name should be a STRING, penalty should be 
	an INT, and new_solution should be a STRING in standard form. """

def write_file(list_solutions):
	filename = "SOLUTIONS RECORDS.txt"
	backup_filename = "SOLUTIONS RECORDS.bak"
	file_exists = os.path.exists(filename) 
	data = []
	for index in range(0, 492):
		data.append(None)
	record_file = None
	if file_exists:
		print("FILE ALREADY EXISTS. OVERWRITING.")
		copyfile(filename, backup_filename)
		file = open(filename, "r")
		data = file.readlines() 
	else:
		for instance in range(0,492):
			record_file = open(filename, "w")
			data[instance] = str(instance + 1) + ": No Algorithm; Penalty|" + str(9999) + "|; No Solution\n"
	for solution in list_solutions:
		instance_number = solution[0]
		algorithm_name = solution[1]
		penalty = solution[2]
		new_solution = solution[3]
		list_tokens = data[instance_number - 1].split("|")
		prev_penalty = int(list_tokens[1])
		if penalty < prev_penalty:
			data[instance_number - 1] = str(instance_number -1) + ": " + algorithm_name + "; Penalty|" + str(penalty) + "|;" + new_solution
	output_file = open(filename, "w")
	output_file.writelines(data)

"""CHANGE THIS OUT WITH YOUR ACTUAL SOLUTION SET (or just call the above method)"""
list_solutions = []
write_file(list_solutions)

