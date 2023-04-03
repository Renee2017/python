import json

def read_data():
 
    new_list = []
    
    with open('C:/Users/lenovo/Desktop/python/execise/info3.json', encoding='utf-8') as f:  
        #执行时cd到execise路径
    
        data = json.load(f)# 列表
        print(data)
# print(data)
 
        for i in data: # i 字典
 
# print((i.get('username'),  i.get('password'), i.get('expect')))
            
            new_list.append((i.get('username'),i.get('password'), i.get('expect')))
            
            # print(new_list)
            
            print( new_list)
read_data()