import yaml

# with open("./data2.yaml", encoding="utf-8") as f:
#     data = yaml.load(f)
#     print(type(data))
#     print(data)

data = {
    "name": "BeJson",
    "page": 88,
    "isNonProfit": True,
    "address": {
        'street': '科技园路.',
        'city': '江苏苏州',
        'country': '中国'
    },
    "links": [
        {'name': 'Google', 'url': 'http://www.google.com'},
        {'name': 'Baidu', 'url': 'http://www.baidu.com'}
    ]
}
with open("./data3.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, encoding='utf-8', allow_unicode=True)

