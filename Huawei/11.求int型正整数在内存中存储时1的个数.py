# 求int型正整数在内存中存储时(计算机底层都是2进制)1的个数


int_num=int(input())
bin_num=bin(int_num) #计算机底层都是2进制，所以2进制强转只需要一个参数
str_num=str(bin_num)
sum=0
for i in str_num:
    if i =='1':#str_num是字符串，i遍历出来的结果是字符，注意写字符'1'
        sum+=1
print(sum)



