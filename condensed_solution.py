read_file = open("SOLUTIONS RECORDS.txt", "r")
write_file = open("Condensed Solution Records", "w")
data = read_file.readlines()
for line in data:
	penalty_tokens = line.split("|")
	instance_tokens = line.split(":")
	instance_number = instance_tokens[0]
	penalty = penalty_tokens[1]
	write_file.write(instance_number + ": " + penalty + "\n")