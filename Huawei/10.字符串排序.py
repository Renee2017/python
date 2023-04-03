# 给定 n 个字符串，请对 n 个字符串按照字典序排列
# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母
# 数据输出n行，输出结果为按照字典序排列的字符串。

n=int(input())
list=[]
for i in range(n):
    str=input()
    list.append(str)
list_new=sorted(list,reverse=True)  # 这里只能用sorted
print(type(list_new)) #<class 'list'>
str='\n'.join(list_new)
print(str)


# sort和sorted的不同
    # 1.sort是应用在list（也就是列表）上的方法，属于列表的成员方法；而sorted是Python内置的全局方法，可以对所有可迭代对象进行排序操作

    # 2.list的sort方法是对已存在的列表进行操作；而内建函数sorted的结果会返回一个新生成的列表，而不是在原有列表的基础上进行操作

    # 3.sort的使用方法为list.sort()，而sorted的使用方法为sorted(list)

