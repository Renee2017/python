# 描述
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

# 输入：

# 合法坐标为A(或者D或者W或者S) + 数字（两位以内）

# 坐标之间以;分隔。

# 非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

# 下面是一个简单的例子 如：

# A10;S20;W10;D30;X;A1A;B10A11;;A10;

# 处理过程：

# 起点（0,0）

# +   A10   =  （-10,0）

# +   S20   =  (-10,-20)

# +   W10  =  (-10,-10)

# +   D30  =  (20,-10)

# +   x    =  无效

# +   A1A   =  无效

# +   B10A11   =  无效

# +  一个空 不影响

# +   A10  =  (10,-10)

# 结果 （10， -10）

direc=input()
list=direc.split(';')
x=0
y=0
address=(x,y)
for i in list:
    if len(i) !=0 & len(i)<=3:
        if i[0]== 'A':
            if i[1] in "123456789" :
                if (i[2] in "0123456789 ") or (i[2] is None):
                    num=int(i.strip('A'))
                    x-=num  # 此处必须写x-=num，不能写x=0-num,因为此代码块可能重复多次执行
                
        if i[0]== 'S':
            if i[1] in "123456789":
                if (i[2] in "0123456789 ") or (i[2] is None):
                    num=int(i.strip('S'))
                    y-=num
        if i[0]== 'D':
            if i[1] in "123456789":
                if (i[2] in "0123456789 ") or (i[2] is None):
                    num=int(i.strip('D'))
                    x+=num
        if i[0]== 'W':
            if i[1] in "123456789":
                if (i[2] in "0123456789 ") or (i[2] is None):
                    num=int(i.strip('W'))
                    y+=num
print("%d,%d"%(x,y))
