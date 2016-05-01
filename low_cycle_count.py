read_file = open("SOLUTIONS RECORDS.txt", 'r')
write_file = open("Low Cycle Count Instances", 'w')
data = read_file.readlines()
for line in data:
	tokens = line.split(":")
	instance_number = tokens[0]
	tokens2 = tokens[1].split(" ")
	print(tokens2[2])
	if tokens2[2] !=  "Algorithm;":
		print("true")
		write_file.write(instance_number + " ")