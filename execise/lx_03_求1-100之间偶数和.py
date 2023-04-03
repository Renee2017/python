# 方法1
i=2
num=0
while i<=100:
    num+=i
    i+=2
print(num)

# 方法2
num=0
i=1
while i<=100:
    if i%2==0: #while中可以嵌套if
        num+=i
    i+=1
print(num)

