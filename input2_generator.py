# In this instance, we specifically target greedy algorithms which work
# by choosing the cycles which are worth the most. Running a greedy algorithm on this 
# instance will result in a cost that is a factor of 4 times worse than the optimal
# solution. 

output = open("TESTINSTANCE2.in", "w")
# We have 500 vertices in out graph.
output.write("500\n")
# We have no child vertices.
output.write("\n")
# We will write in cycles of 20.
for cycle in range (0,500,20):
	# We define our offset to be added to each node.
	start = cycle//20 * 20
	end = start + 20
	#We can now construct edges for the cycle we are focusing on.
	for node_a in range (0, 20):
		# For nodes not in our cluster, there should be no cycles.
		for node in range (0, start):
			output.write("0 ")
		# We start considering nodes in our cluster.
		for node_b in range (0, 20):
			# We connect the 4 central patients into one cycle, 
			# all adults, with a total value of 5. 
			if node_a == 0:
				if node_b == 1 or node_b == 5:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 1:
				if node_b == 2 or node_b == 8:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 2:
				if node_b == 3 or node_b == 11:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 3:
				if node_b == 4 or node_b == 14:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 4:
				if node_b == 0 or node_b == 17:
					output.write("1 ")
				else:
					output.write("0 ")
			# We now connect the first of four other cycles,
			# each cycle consisting of all adults
			# with a total value of 4. 
			if node_a == 5:
				if node_b == 6:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 6:
				if node_b == 7:
					output.write("1 ")
				else:
					output.write("0 ")	
			if node_a == 7:
				if node_b == 0:
					output.write("1 ")
				else:
					output.write("0 ")
			# side cycle 2
			if node_a == 8:
				if node_b == 9:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 9:
				if node_b == 10:
					output.write("1 ")
				else:
					output.write("0 ")	
			if node_a == 10:
				if node_b == 1:
					output.write("1 ")
				else:
					output.write("0 ")
			# side cycle 3
			if node_a == 11:
				if node_b == 12:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 12:
				if node_b == 13:
					output.write("1 ")
				else:
					output.write("0 ")	
			if node_a == 13:
				if node_b == 2:
					output.write("1 ")
				else:
					output.write("0 ")
			# side cycle 4
			if node_a == 14:
				if node_b == 15:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 15:
				if node_b == 16:
					output.write("1 ")
				else:
					output.write("0 ")	
			if node_a == 16:
				if node_b == 3:
					output.write("1 ")
				else:
					output.write("0 ")
			# side cycle 5
			if node_a == 17:
				if node_b == 18:
					output.write("1 ")
				else:
					output.write("0 ")
			if node_a == 18:
				if node_b == 19:
					output.write("1 ")
				else:
					output.write("0 ")	
			if node_a == 19:
				if node_b == 4:
					output.write("1 ")
				else:
					output.write("0 ")
		#All vertices not part of this cluster should have no edges to this cluster.
		for node in range (end, 500):
			output.write("0 ")
		output.write("\n")




