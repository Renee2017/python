num=input("请输入一串数字")
num1=list(num[::-1])
list_new=[]
for i in num1:
    if i not in list_new:#去重
        list_new.append(i)
str=''.join(list_new)
print(str)

