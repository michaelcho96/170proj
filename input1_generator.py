output = open("TESTINSTANCE1.in", "w")
output.write("500\n")
for node in range(0, 500, 2):
	output.write(str(node) + " ")
output.write("\n")
for node_a in range(0, 500):
	for node_b in range(0, 500):
		if node_a != node_b:
			output.write("1 ")
		else:
			output.write("0 ")
	output.write("\n")