my_list = [3, 2, 4, 1, 2, 3, 3, 2, 1, 2, 3, 1]
print(list(set(my_list))) #方法1,set方法出来的结果顺序是随机的


new_list=[]
for i in my_list:
    if i in new_list:
        continue #continue表示跳过此次循环，重新循环，pass表示占位，后面仍然会执行
    else:
        new_list.append(i)
print(new_list)
