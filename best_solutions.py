import os.path
import io
from shutil import copyfile

""" STORES THE BEST SOLUTIONS """
""" HOW TO USE: You should input a list of solutions. Each 
	solution should be in this form: [instance number, algorithm_name, penalty, new_solution ].
	The instance_number should be an INT, algorithm_name should be a STRING, penalty should be 
	an INT, and new_solution should be a STRING in standard form. """

def write_file(output_file, list_solutions):
	backup_filename = output_file + ".bak"
	file_exists = os.path.exists(output_file) 
	data = []
	for index in range(0, 492):
		data.append(None)
	record_file = None
	if file_exists:
		# print("FILE ALREADY EXISTS. OVERWRITING.")
		copyfile(output_file, backup_filename)
		file = open(output_file, "r")
		data = file.readlines() 
	else:
		for instance in range(0,492):
			record_file = open(output_file, "w")
			data[instance] = str(instance + 1) + ": No Algorithm; Penalty|" + str(9999) + "|; No Solution\n"
	for solution in list_solutions:
		instance_number = solution[0]
		algorithm_name = solution[1]
		penalty = solution[2]
		new_solution = solution[3]
		list_tokens = data[instance_number - 1].split("|")
		prev_penalty = int(list_tokens[1])
		if penalty <= prev_penalty:
			data[instance_number - 1] = str(instance_number) + ": " + algorithm_name + ", Penalty|" + str(penalty) + "| " + new_solution + "\n"
	output_file = open(output_file, "w")
	output_file.writelines(data)

# write_file([])



