import os

with open('E:\\stud\\spark\\author_book\\book_names.txt', 'r') as f:
	lines = f.readlines()
	names = []

	for txt in os.listdir('E:\\stud\\spark\\books'):
		names.append(txt[:txt.find('.')])

	for i in range(len(lines)):
		lines[i] = lines[i][lines[i].find(' ') + 1 : -1]

	for name in names:
		if not (name in lines):
			print(name)

	for line in lines:
		if not (line in names):
			print(line)
