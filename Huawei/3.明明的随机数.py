# 明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

# 数据范围：1≤N≤1000,   输入的数字大小满足 1≤val≤500 
N = int(input())
if N>=1 & N<=1000 :
    num = []
    i = j = 0
    while i < N:#i表示第几次输入
        current_num = int(input())
    
        if current_num not in num:
            num.append(current_num)
    
        i += 1
    
    num.sort()
    
    for j in range(len(num)):
        print(num[j])
