import os.path
import io
from shutil import copyfile

filename = "SOLUTIONS RECORDS.txt"
backup_filename = "SOLUTIONS RECORDS.bak"
copyfile(backup_filename, filename)