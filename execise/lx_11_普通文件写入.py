
f=open('a.txt','w',encoding="utf-8")
print('ok')
f.write('so sad')
f.close()

with open('a.txt',"w",encoding='utf-8') as ff:
    print('11')
    ff.write('sad')
    

