import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument("arg1", help="description of arg1")
# Add another argument
parser.add_argument("arg2", help="description of arg2")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the argument
print(type(args.arg1))
print(f"{args.arg1.split()}")
print(f"arg2: {args.arg2}")