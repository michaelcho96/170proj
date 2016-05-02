from utils import validate_formatted_solution

file = open("SOLUTIONS RECORDS.txt", "r")
data = file.readlines()
for line in data:
	tokens = line.split("|")
	number_tokens = line.split(":")
	instance_number = int(number_tokens[0])
	solution = tokens[2]
	if not validate_formatted_solution(solution):
		print("solution invalid.")
		data[instance_number - 1] = str(instance_number) + ": No Algorithm; Penalty|" + str(9999) + "|; No Solution\n"
file = open("SOLUTIONS RECORDS.txt", "w")
file.writelines(data)