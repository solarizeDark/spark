import os

with open('E:\\stud\\spark\\to_del', 'w') as to_del:

    for name in os.listdir('E:\\stud\\spark\\books'):
        if os.path.getsize('E:\\stud\\spark\\books\\' + name) / 1024 < 3:
            to_del.write(name + '\n')
