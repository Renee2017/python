def calc(a, b):
    num = a + b
    num1 = a - b
    return num, num1
# 写法⼀
result = calc(10, 5)
print(result)
# 写法⼆, 直接拆包
x, y = calc(20, 10)
print(x,y)

