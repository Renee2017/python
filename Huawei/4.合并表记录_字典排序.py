# 数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。

# 输入描述：
# 先输入键值对的个数n（1 <= n <= 500）
# 接下来n行每行输入成对的index和value值，以空格隔开

# 输出描述：
# 输出合并后的键值对（多行

n=int(input('请输入键值对个数'))
dict={}
for i in range(n):
    z=input("请输入成对的键值对，用空格隔开")
    #map()函数接收两个参数，一个是函数，一个是Iterable（不断更新），map将传入的函数依次作用到序列的每一个元素，并把结果作为新的Iterable返回
    #字符串中包含空格时 如：0 3，无法直接转换为整数格式，必须先通过split转换为列表格式，再转换为整数格式
    (x,y)=map(int,z.split())
    if x in dict.keys():
        dict[x]+=y
    else:
        dict[x]=y
#字典排序不用.sort,用sorted(),如果是按值排序，还要用到匿名函数：变量=sorted(student_dict.items(), key=lambda x: x[1], reverse=True)。如果按键排序，可以直接sorted(dict.keys),keys可以省略
for index in sorted(dict):
    print(index,dict[index])

# 第一种：最常见的单个字典格式数据排序
    # 字典排序
    # a = {'a': 3, 'c': 89, 'b': 0, 'd': 34}
    # # 按照字典的值进行排序
    # a1 = sorted(a.items(), key=lambda x: x[1])
    # # 按照字典的键进行排序
    # a2 = sorted(a.items(), key=lambda x: x[0])
    # print('按值排序后结果', a1)
    # print('按键排序后结果', a2)
    # print('结果转为字典格式', dict(a1))
    # print('结果转为字典格式', dict(a2))
# 第二种：字典列表排序
#     b = [{'name': 'lee', 'age': 23}, {'name': 'lam', 'age': 12}, {'name': 'lam', 'age': 18}]
#     b1 = sorted(b, key=lambda x: x['name'])
#     b2 = sorted(b, key=lambda x: x['age'],  reverse=True)
#     b3 = sorted(b, key=lambda x: (x['name'], -x['age']))
#     print('按name排序结果：', b1)
#     print('按age排序结果：', b2)
#     print('name相同按age降序排列：', b3)

