import os
from transliterate import translit

for name in os.listdir('E:\\stud\\spark\\books'):
    try:
        reader = open('E:\\stud\\spark\\books' + '\\' + name, 'r', encoding='ansi')
        lines = reader.readlines()
    except UnicodeDecodeError:
        reader = open('E:\\stud\\spark\\books' + '\\' + name, 'r', encoding='utf-8')
        lines = reader.readlines()

    for i in range(len(lines)):
        if lines[i] == '\n':
            continue
        if 'e' in lines[i].lower():
            lines[i] = lines[i].lower().replace('e', translit('e', 'ru'))
        if 'a' in lines[i].lower():
            lines[i] = lines[i].lower().replace('a', translit('a', 'ru'))
        if 'o' in lines[i].lower():
            lines[i] = lines[i].lower().replace('o', translit('o', 'ru'))
        if 'p' in lines[i].lower():
            lines[i] = lines[i].lower().replace('p', translit('r', 'ru'))
        if 'c' in lines[i].lower():
            lines[i] = lines[i].lower().replace('c', translit('s', 'ru'))
        if 'y' in lines[i].lower():
            lines[i] = lines[i].lower().replace('y', translit('u', 'ru'))
        if 'x' in lines[i].lower():
            lines[i] = lines[i].lower().replace('x', translit('h', 'ru'))

    with open('E:\\stud\\spark\\books' + '\\' + name, 'w', encoding='utf-8') as writer:
        for line in lines:
            writer.write(line)
