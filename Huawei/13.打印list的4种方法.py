# 1.用for循环来打印

a = [1, 2, 3, 4, 5]
for x in range(len(a)):
    print (a[x])
# 结果
# 1 2 3 4 5

# 2.用 * 星号来打印
a = [1, 2, 3, 4, 5]
# 默认用空格分隔
print(*a)
# 用逗号分隔
print(*a, sep = ", ")
# 用行分隔
print(*a, sep = "\n")
# 结果
# 1 2 3 4 5
# 1, 2, 3, 4, 5
# 1
# 2
# 3
# 4
# 5

# 3.把list转换为str来打印
# 如果list里面是str的话，直接用join（）函数来加入空格
a =["Geeks", "for", "Geeks"]
print(' '.join(a))
# 如果是数字的话，先转换为str
a = [1, 2, 3, 4, 5]
print (str(a)[1:-1])
# 结果
    # Geeks for Geeks
    # 1, 2, 3, 4, 5

# 4.用map把数组里非字符类型的数据转换为字符，然后打印
#加入空格
a = [1, 2, 3, 4, 5]
print(' '.join(map(str, a)))
#换行打印
print('\n'.join(map(str, a)))
    # 结果
    # 1 2 3 4 5
    # 1
    # 2
    # 3
    # 4
    # 5