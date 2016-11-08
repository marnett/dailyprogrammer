import sys

def main(argv):
	
	filename = argv[0]
	file = open(filename, 'r')

	#save weight and max temperature
	input_line = file.readline()
	weight_and_temp = input_line.split()
	weight = weight_and_temp[0]
	max_temp = weight_and_temp[1]

	chairs = []
	itr = 1

	#loop through inputs and decide where she can sit and eat
	for x in file.readlines():
		line = x.split()
		chair_max_weight = line[0]
		porridge_temp = line[1]

		if int(chair_max_weight) > int(weight) and int(porridge_temp) < int(max_temp):
			chairs.append(itr)

		itr+=1

	#print results
	for chair in chairs:
		print chair



if __name__ == '__main__':
	main(sys.argv[1:])