def read():
    file = open('test.txt', encoding='utf-8')
    data = file.read()
    print(data)
    file.close()


def read_lines():
    file = open('test.txt', encoding='utf-8')
    data_lines = file.readlines()
    print(len(data_lines))
    for line in data_lines:
        print(line)
    file.close()


def write():
    file = open('test3.txt', 'a', encoding='utf-8')
    file.write('hello你好啊11\n')

    file.writelines(['李白\n', '李太白'])
    file.close()


read()
read_lines()
write()