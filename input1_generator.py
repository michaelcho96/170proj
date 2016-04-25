# This creates a graph where every vertex has a directed edge
# to every other vertex. This is a hard input for very naive 
# solutions.
# While the concept may be used, this IN NO WAY a submittable
# input. Any half-assed algorithm will immediatly negate all
# pairs and return the optimal solution in no time at all. 

output = open("TESTINSTANCE1.in", "w")
output.write("500\n")
# We have no child nodes.
output.write("\n")
for node_a in range(0, 500):
	for node_b in range(0, 500):
		if node_a != node_b:
			output.write("1 ")
		else:
			output.write("0 ")
	output.write("\n")