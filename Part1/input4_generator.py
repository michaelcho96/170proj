output = open("TESTINSTANCE4.in", "w")
output.write("500\n")
# No children
output.write("\n")
# Building our cycled clusters which each contain 5 nodes
for cluster in range (0, 500, 5):
	start = cluster//5 * 5
	end = start + 5
	#We can now construct edges for the cycle we are focusing on.
	for node_a in range (0, 5):
		# For nodes not in our cluster, there should be no cycles.
		for node in range (0, start - 1):
			output.write("0 ")
		if node_a == 0:
			if start != 0:
				output.write("1 ") # No edge to last cluster
			output.write("0 ") # No edge to 0
			output.write("0 ") # No edge to 1 
			output.write("0 ") # No edge to 2
			output.write("1 ") # Edge to 3
			output.write("0 ") # No edge to 4
			if start != 495:
				output.write("0 ") # No edge to next cluster
		if node_a == 1:
			if start != 0:
				output.write("0 ") # No edge to last cluster
			output.write("0 ") # No edge to 0
			output.write("0 ") # No edge to 1 
			output.write("0 ") # No edge to 2
			output.write("0 ") # No edge to 3
			output.write("1 ") # Edge to 4
			if start != 495:
				output.write("0 ") # No edge to next cluster
		if node_a == 2:
			if start != 0:
				output.write("0 ") # No edge to last cluster
			output.write("0 ") # No edge to 0
			output.write("0 ") # No edge to 1 
			output.write("0 ") # No edge to 2
			output.write("0 ") # No edge to 3
			output.write("1 ") # Edge to 4
			if start != 495:
				output.write("0 ") # No edge to next cluster
		if node_a == 3:
			if start != 0:
				output.write("0 ") # No edge to last cluster
			output.write("1 ") # Edge to 0
			output.write("1 ") # Edge to 1 
			output.write("1 ") # Edge to 2
			output.write("0 ") # No edge to 3
			output.write("0 ") # No edge to 4
			if start != 495:
				output.write("0 ") # No edge to next cluster
		if node_a == 4:
			if start != 0:
				output.write("0 ") # No edge to last cluster
			output.write("0 ") # No edge to 0
			output.write("0 ") # No edge to 1 
			output.write("0 ") # No edge to 2
			output.write("1 ") # Edge to 3
			output.write("0 ") # Edge to 4
			if start != 495:
				output.write("1 ") # No edge to next cluster
		for node in range (end + 1, 500):
			output.write("0 ")
		output.write("\n")

