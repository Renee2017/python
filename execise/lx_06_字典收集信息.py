dict={}
list=[]
for i in range(3):
    name=input('请输入你的姓名')
    age=input('请输入你的年龄')
    dict['name']=name
#     字典[键] = 数据值
# 1. 如果键已经存在,就是修改数据值
# 2. 如果键不存在,就是添加数据(即添加键值对)
    dict['age']=age
    list.append(dict)
print(list)

my_list = [{'id': 1,'money': 10}, {'id': 2,'money': 20}]
for item in my_list:
    print(item['id'],item['money'])
