import os

def  main(path):
	names = ['Petru', 'Mihai', 'Emanuel']
	extractaed_names = list()

	if not os.path.exists(path):
		with open(path, 'w') as output_file:
			for name in names:
				output_file.write(name + '\n')

	with open(path, 'r') as input_file:
		for line in input_file:
			extractaed_names.append(line.strip())

	print(names == extractaed_names)
	print(extractaed_names)

if __name__ == '__main__':
	file_path = '/Users/petru/Code/Problems/General Problems/Python/names.txt'
	main(file_path)
