import json
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))
""" json.dumps()函数将Python对象转换为JSON字符串，方便我们进行数据交换和存储。
with open('data.json', 'w') as f:
    json.dump(my_dict, f)
"""
with open('对象序列化和反序列化\data.json', 'r') as f:
    data = json.load(f)
print(data)