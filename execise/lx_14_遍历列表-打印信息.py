# 通过 input输⼊3个⼈信息，每个⼈有姓名和年龄，将信息存⼊字典中，并将将字典存⼊列表。
my_list = []
for i in range(3):
    my_dict = {} # 每循环⼀次创建⼀个字典
    name = input('请输⼊姓名:')
    age = input('请输⼊年龄:')
    my_dict['name'] = name
    my_dict['age'] = age
    print(my_dict)
    my_list.append(my_dict)
for item in my_list: 
    print(item['name'], item['age']) 