import math
num=float(input())
a,b=math.modf(num) #该函数modf()用于将传递的参数拆分为小数和整数
if a >=0.5:
    result=int(b+1)
else:
    result=int(b)
print(result)
