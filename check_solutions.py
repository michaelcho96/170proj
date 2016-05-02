from utils import comprehensive_solution_validation
from utils import create_graph

file = open("COMBINED SOLUTIONS", "r")
data = file.readlines()
valid = True
for line in data:
	tokens = line.split("|")
	number_tokens = line.split(":")
	instance_number = int(number_tokens[0])
	solution = tokens[2]
	filename = "instances/" + str(instance_number) + ".in"
	G = create_graph(filename)
	print("Checking instance " + str(instance_number))
	if not (comprehensive_solution_validation(solution,G)):
		valid = False
		print("solution " + str(instance_number) + " invalid.")
	else:
		print("solution " + str(instance_number) + " valid.")
		
print("Scan complete.")
if valid:
	print("All instances valid")
else:
	print("One or more instances are invalid")

