import os
import string

alphabet_low = set(string.ascii_lowercase)
alphabet_up = set(string.ascii_uppercase)

def black_list(lines):
	cnt = 0
	black_list=[]
	for key in lines.keys():
		for i in range(len(lines[key])):
			if lines[key][i] in alphabet_low or lines[key][i] in alphabet_up:
				cnt += 1
		if cnt / len(lines[key]) > 0.1:
			black_list.append(key)
		cnt = 0
	return black_list

l = {}
for file in os.listdir('E:\\stud\\spark\\books'):
	with open('E:\\stud\\spark\\books' + '\\' + file, 'r') as f:
		lines = f.readlines()
		for i in range(int(len(lines) / 2), int(len(lines) / 2) + 20):
			if len(lines[i]) > 20:
				l[file] = lines[i]
				break

with open('E:\\stud\\spark\\to_del', 'w') as to_del:
	for book in black_list(l):
		to_del.write(book + '\n')