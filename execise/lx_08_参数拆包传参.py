def my_sum(*args, **kwargs):
    num = 0
# 定义变量,保存求和的结果
    for i in args:
        num += i
    for j in kwargs.values():
        num += j
    print(num)
my_list = [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_sum(*my_list)
my_sum(**my_dict)
my_sum(*my_list, **my_dict)