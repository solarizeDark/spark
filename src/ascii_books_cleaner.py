import os

with open('E:\\stud\\spark\\to_del', 'r', encoding='utf-8') as file:
	books = file.readlines()

# for i in range(len(books)):
# 	books[i] = books[i][:-1]
#
with open('E:\\stud\\spark\\author_book\\book_names.txt', 'r') as reader:
	lines = reader.readlines()

	for book in books:
		for line in lines:
			if book[:-5] == line[line.find(' ') + 1 : line.rfind(' ')]:
				lines.remove(line)

with open('E:\\stud\\spark\\author_book\\book_names.txt', 'w') as writer:
	for line in lines:
		writer.write(line)

# for i in range(len(books)):
# 	books[i] = books[i] + '.txt'

for name in books:
	if name[:-1] in os.listdir('E:\\stud\\spark\\books\\'):
		os.remove('E:\\stud\\spark\\books\\' + name[:-1])