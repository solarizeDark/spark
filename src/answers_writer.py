
with open('E:\\stud\\spark\\author_book\\book_names.txt', 'r') as reader:
	lines = reader.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i][:-1] + ' 1\n'
		print(lines[i])

with open('E:\\stud\\spark\\author_book\\book_names.txt', 'w') as writer:
	writer.writelines(lines)
