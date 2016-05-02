import os.path
import io
from shutil import copyfile

filename = "SOLUTIONS RECORDS.txt"
backup_filename = "SOLUTIONS RECORDS - M.txt"
copyfile(backup_filename, filename)
file = open("SOLUTIONS RECORDS - M.txt", "w")
file = open("SOLUTIONS RECORDS - M.bak", "w")