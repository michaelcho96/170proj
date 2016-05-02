from utils import read_solution_line

write_file = open("solutions.out", "w")
read_file = open("COMBINED SOLUTIONS", "r")
data = read_file.readlines()
for line in data:
	info = read_solution_line(line)
	solution = info[3]
	if solution.isspace():
		print("No solution")
		write_file.write("None\n")
	else:
		solution = solution[1:]
		write_file.write(solution + "\n")
