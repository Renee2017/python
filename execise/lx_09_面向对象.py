print(chr(97))
print(id(6))
class Cat:
    #1.设计类
    def eat(self): # self 会⾃动出现,暂不管
 
        print(f'{id(self)}, self')
 
        print('⼩猫爱吃⻥...')
# 2. 创建对象
blue_cat = Cat()
print(f'{id(blue_cat)}, blue_cat')
# 3. 通过对象调⽤类中的⽅法
blue_cat.eat() # blue_cat 对象调⽤ eat ⽅法, 解释器就会将 blue_cat 对象传给 self