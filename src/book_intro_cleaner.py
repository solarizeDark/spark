import os

for name in os.listdir('E:\\stud\\spark\\books'):
    with open('E:\\stud\\spark\\books' + '\\' + name, 'r', encoding='ansi') as reader:
        lines = reader.readlines()
        to_write = []
        for i in range(7, len(lines) - 7):
            to_write.append(lines[i])

    with open('E:\\stud\\spark\\books' + '\\' + name, 'w', encoding='utf-8') as writer:
        for line in to_write:
            writer.write(line)