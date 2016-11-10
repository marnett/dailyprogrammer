import sys

def main(argv):
	
	with open(argv[0], 'r') as f:
		file = f.read()

	content = file.split()
	print content
	set = ['+','-','*','x','/','//','%','^','!']

	for x in content:
		if x not in set:
			print float(x)


if __name__ == "__main__":
	main(sys.argv[1:])