import sys

def main(argv):
	with open(argv[0], 'r') as f:
		for line in f:
			min,max = map(int,line.split())
			for x in range(min, max+1):
				square = x**2
				for i in xrange(len(str(square))):
					#print i+1, square
					left, right = str(square)[:i+1], str(square)[i+1:]
					if len(right) == 0:
						right = 0
					if int(right) != 0:
						sum = int(left) + int(right)
						if sum == x:
							print x,
			print "\n"
			
if __name__ == "__main__":
	main(sys.argv[1:])