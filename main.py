import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument("arg1", help="description of arg1")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the argument
print(f"arg1: {args.arg1}")