from utils import read_solution_line

file_a = "SOLUTIONS RECORDS.txt"
file_b = "SOLUTIONS RECORDS - M.txt"

def combine(a, b):
	write_file = open("COMBINED SOLUTIONS", "w")
	file_a = open(a, "r")
	file_b = open(b, "r")
	data_a = file_a.readlines()
	data_b = file_b.readlines()
	for index in range(0,492):
		line_a = read_solution_line(data_a[index])
		line_b = read_solution_line(data_b[index])
		if line_a[2] < line_b[2]:
			write_file.write(data_a[index])
		else:
			write_file.write(data_b[index])

combine(file_a, file_b)