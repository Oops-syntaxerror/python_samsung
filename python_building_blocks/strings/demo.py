import sys

try:
    arg1 = sys.argv[1]  # First argument after the script name
    arg2 = sys.argv[2]  # Second argument after the script name
    print(f"Argument 1: {arg1}, Argument 2: {arg2}")
except IndexError:
    print("Error: Not enough arguments provided.")
    print("Usage: python script.py <arg1> <arg2>")
