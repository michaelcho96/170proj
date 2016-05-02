from utils import combine
import sys
import os.path
import io
from shutil import copyfile

if len(sys.argv) != 2:
	print("Usage: combine_solutions.py [file1]")
else:		
	file = sys.argv[1]
	combine("COMBINED SOLUTIONS", file)
	copyfile("COMBINED SOLUTIONS", "CURRENT BEST SOLUTIONS")
	print("Copied new solutions to CURRENT BEST SOLUTIONS.")
	print("Done.")