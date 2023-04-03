my_list = [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
# 将字典和列表中的数据使⽤ my_sum 函数进⾏求和, 如何传参
def my_sum(*args, **kwargs):
    num=0
    for i in args:
        num=num+i
    for j in kwargs.values():
        num=num+j
    print(num)


my_sum(*my_list) #拆包后进行不定长位置传参
my_sum(**my_dict)  #拆包后进行不定长关键字传参