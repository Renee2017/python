# 定义变量 姓名  年龄  身高 及格率
name = '小明' 
age = 18   
height = 1.71 
rate=90 
# 要求按照以下个数输出个人信息
# 我的名字是 xx, 年龄是 xx, 身高是 xx m
# 使用格式化输出实现
# print('我的名字是 name, 年龄是 age, 身高是 height m')
print(f'我的名字是{name}, 年龄是{age}, 身高是{height}，及格率是{rate}%')
# %s字符串占位符， %d整数占位符，%f 小数占位符，%06d整数部分有6位， %2f小数部分有两位)
print(f'我的名字是{name}, 年龄是{age:06d}, 身高是{height:.2f}，及格率是{rate}%')
