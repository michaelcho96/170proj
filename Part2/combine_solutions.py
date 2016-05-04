from utils import combine
import sys
import os.path
from utils import read_solution_line
from shutil import copyfile

if len(sys.argv) != 2:
	print("Usage: combine_solutions.py [file1]")
else:		
	file = sys.argv[1]
	combine("COMBINED SOLUTIONS", file)
	copyfile("COMBINED SOLUTIONS", "CURRENT BEST SOLUTIONS")
	print("Copied new solutions to CURRENT BEST SOLUTIONS.")
	print("Done.")
	# Writing to solutions.out
	print("Writing to solutions.out")
	write_file = open("solutions.out", "w")
	read_file = open("COMBINED SOLUTIONS", "r")
	data = read_file.readlines()
	for line in data:
		info = read_solution_line(line)
		solution = info[3]
		if solution.isspace():
			write_file.write("None\n")
		else:
			solution = solution[1:]
			write_file.write(solution + "\n")
	print("Done.")
