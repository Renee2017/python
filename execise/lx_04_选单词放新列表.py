# 选出list1中以s或e结尾的单词放在新列表
list1=['red','apples','orange','pink','bananas','blue','black','white']
list_new=[]
for i in list1:
    if i[-1]=='s' or i[-1]=='e':
        list_new.append(i)
print(list_new)