import networkx as nx 

def main(argv):
	if len(argv != 1):
		print "Please input a .in file to process."

def convert(input_filename):
	input_file = open(input_filename, "r")
	number_of_vertices = input_file.readline()
	child_vertices = input_file.readline()
	adjacency_list = []
	while input_file.readline() != '':
		adjacency_list.append(input_file)