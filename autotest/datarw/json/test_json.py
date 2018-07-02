import json


def transfer():
    """python字典与JSON之间的转换"""

    # Python 字典类型转换为 JSON 字符串
    data1 = {
        'id': 1,
        'name': 'Tom',
        'address': '北京市海淀区',
        'school': None
    }
    json_str = json.dumps(data1)
    print(data1)
    print(json_str)
    print(type(data1))
    print(type(json_str))

    # 将 JSON 字符串转换为 Python 字典
    data2 = json.loads(json_str)
    print(data2)
    print(type(data2))


def read():
    """读取JSON文件"""

    with open('json.txt', encoding='UTF-8') as f:
        data = json.load(f)
        print(data)
        name = data['name']
        print('name=', name)

        address = data['address']
        city = address['city']
        print('city=', city)

        links = data['links']
        print(len(links))
        for link in links:
            print(link)


def create():
    """创建JSON文件"""

    param = {'name': 'tom', 'age': 20}
    with open('json-new.txt', 'w', encoding='UTF-8') as f:
        json.dump(param, f)


transfer()
# read()
# create()
