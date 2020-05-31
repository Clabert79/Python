"""
Usage:
    script_name.py [-a] [-b] [-c] <path>

Options:
    -a            Print all the things.
    -b            Get more bees into the path.
"""
from docopt import docopt

if __name__ == "__main__":
	args = docopt(__doc__)
	print(args)
