# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
# 数据范围：1≤n≤1000 
import sys

# def strSelectCounter():
for line_01 in sys.stdin:  #sys.stdin 系统标准输入
    for line_02 in sys.stdin:
        """将输入的字符串全部转换为大写并剔除输入字符串中的空格"""
        a=line_01.upper().strip()
        b=line_02.upper().strip()
        Counter=0
        for A in a:
            for B in b:
                if B==A:
                    Counter+=1
        print (Counter) #注意print的位置一定是跳出循环，不然打印的是每次的counter