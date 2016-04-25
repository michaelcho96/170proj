# In this instance, we specifically target greedy algorithms which work
# by choosing the cycles which are worth the most. Running a greedy algorithm on this 
# instance will result in a cost that is a factor of 9/4 worse than the best case.

# While this is submittable, this could be made better by having cluster where
# the central node consists of five nodes of value 4, while there are five 
# side-cylces each with a value of 4. The greedy solution would then be a factor
# of 4 worse than the optimal solution. 

output = open("TESTINSTANCE2.in", "w")
# We have 500 vertices in out graph.
output.write("500\n")
# We have no child vertices.
output.write("\n")
# We will write in cycles of 20.
for cycle in range (0,500,10):
	# We define our offset to be added to each node.
	start = cycle//10 * 10
	end = start + 10
	#We can now construct edges for the cycle we are focusing on.
	for node_a in range (0, 10):
		# For nodes not in our cluster, there should be no cycles.
		for node in range (0, start):
			output.write("0 ")
		# We start considering nodes in our cluster.
		for node_b in range (0, 10):
			# We connect the 4 central patients into one cycle, 
			# all adults, with a total value of 4. 
			# We use node_index of 0 as the connecting node to 
			# all other nodes.
			if node_a == 0:
				if node_b == 1 or node_b == 4:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 1:
				if node_b == 2 or node_b == 6:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 2:
				if node_b == 3 or node_b == 8:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 3:
				if node_b == 0:
					output.write("1 ")
				else:
					output.write("0 ")
			# We now connect the first of two other cycles,
			# each cycle consisting of all adults
			# with a total value of 3. 
			if node_a == 4:
				if node_b == 5:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 5:
				if node_b == 0:
					output.write("1 ")
				else:
					output.write("0 ")	
			# side cycle 2
			if node_a == 6:
				if node_b == 7:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 7:
				if node_b == 1:
					output.write("1 ")
				else:
					output.write("0 ")	
			# side cycle 3
			if node_a == 8:
				if node_b == 9:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 9:
				if node_b == 2:
					output.write("1 ")
				else:
					output.write("0 ")	
		#All vertices not part of this cluster should have no edges to this cluster.
		for node in range (end, 500):
			output.write("0 ")
		output.write("\n")




