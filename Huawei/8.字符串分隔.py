# 输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
mystr = input()
 
length = len(mystr)
# str = str.split()
a = length / 8
b = length % 8
if b == 0:
    for i in range(int(a)):
        print(mystr[ 8 *i : 8 * (i + 1)])
else:
    for i in range(int(a)):
        print(mystr[8 * i : 8 * (i + 1)])
    print(mystr[-b:]+"0"*int(8-b))
