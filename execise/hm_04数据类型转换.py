age=input("请输入你的年龄:")
print("转换前age的类型：",type(age))
age1=int(age)
print("转换后age的类型",type(age))
print("转换后age1的类型",type(age1))
age2=str(age1)
print("转换后age2的类型",type(age2))
print(age2)

# int()  将其他类型转换为 int 类型
# 可以将 float类型的数字转换为 整型
height=1.9
print(type(height))
height2=int(height)
print(type(height2))
# 可以将 整数类型的字符串 转换为 整型 3 123  
print(height2)
#小数转整数默认取较小值，比如1.9转为整数是1，不是2
