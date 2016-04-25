# In this instance, we specifically target Dynamic Programming.


output = open("TESTINSTANCE3.in", "w")
# We have 500 vertices in out graph.
output.write("500\n")
# We have only child vertices.
for n in range(0, 500):
	output.write(str(n) + " ")
output.write("\n")
for x in range (0, 500):
	for y in range(0, 500):
		if x == y:
			output.write("0 ")
		else:
			if x % 5 == 0 or y % 5 == 0:
				output.write("1 ")
			else:
				output.write("0 ")
	output.write("\n")


	