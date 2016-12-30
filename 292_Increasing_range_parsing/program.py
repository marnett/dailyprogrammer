import sys, re

def main(argv):
	
	with open(argv[0], 'r') as f:
		file = f.readlines()

	for line in file:
		pattern = r'\"(.*?)\"'
		match = re.findall(pattern, line)
		lst = match[0].split(",")
		print line
		for x in lst:
			print x



if __name__ == "__main__":
	main(sys.argv[1:])