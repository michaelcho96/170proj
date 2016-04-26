# This creates a graph where every vertex has a 50% chance of having a directed edge to another vertex
from random import randint

k = randint(350, 500)

output = open("TESTINSTANCE5.in", "w")
output.write(str(k) + "\n")
# 1 in 3 vertices are child nodes
for n in range(0, k):
	if randint(0, 2) == 2:
		output.write(str(n) + " ")
output.write("\n")
for node_a in range(0, k):
	for node_b in range(0, k):
		if node_a != node_b and randint(0, 1) == 1:
			output.write("1 ")
		else:
			output.write("0 ")
	output.write("\n")