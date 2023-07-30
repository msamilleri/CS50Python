from tabulate import tabulate
import sys
import csv
if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 2):
    sys.exit("Too many command-line arugments")
file_python = sys.argv[1]
if not file_python.endswith(".py"):
    sys.exit("Not a Python File")

try:
    with open(file_python) as file:
        lines_of_code = 0
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if not line.startswith("#") and line != "":
                lines_of_code += 1
        print(lines_of_code)
except FileNotFoundError:
    sys.exit("File does not exist")