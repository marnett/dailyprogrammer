import sys

def main(argv):

	### Open input file ###
	with open(argv[0], 'r') as f:
		file = f.read()

	### Split the input words ###
	words = file.splitlines()
	starting_word = words[0]
	ending_word = words[1]

	### Manipulate starting word to get ending word ###
	print starting_word
	for i in range(len(starting_word)):
		if starting_word[i] != ending_word[i]:
			print ending_word[:i+1] + starting_word[i+1:]

if __name__ == "__main__":
	main(sys.argv[1:])