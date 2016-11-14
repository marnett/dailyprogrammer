import sys
import math

def main(argv):
	
	with open(argv[0], 'r') as f:
		file = f.read()

	content = file.split()
	set = ['+','-','*','x','/','//','%','^','!']

	#loop through content and add floats to stack
	stack = []

	for x in content:
		if x not in set:
			stack.append(float(x))
		else:
			current = x
			if current == '+':
				input1 = stack.pop()
				input2 = stack.pop()
				result = float(input1 + input2)
				stack.append(result)
			elif current == '-':
				input1 = stack.pop()
				input2 = stack.pop()
				result = float(input2 - input1)
				stack.append(result)
			elif current == '*' or current == 'x':
				input1 = stack.pop()
				input2 = stack.pop()
				result = float(input1*input2)
				stack.append(result)
			elif current == '/':
				input1 = stack.pop()
				input2 = stack.pop()
				result = float(input2/input1)
				stack.append(result)
			elif current == '//':
				print current
			elif current == '%':
				print current
			elif current == '^':
				power = stack.pop()
				base = stack.pop()
				result = float(base**power)
				stack.append(result)
			elif current == '!':
				input1 = stack.pop()
				result = float(math.factorial(input1))
				stack.append(result)
	
	#print final result
	print stack.pop()

if __name__ == "__main__":
	main(sys.argv[1:])