

# 让三个学生输入名字后，抽签选学生
import random
name_list=[]
for i in range(3):
    i=input('请输入名字')
    name_list.append(i)
print(name_list)
order=0
while order<5:
    num=random.randint(0,2) #包含三个数——0、1、2
    print(num)
    print(name_list[num])
    order+=1