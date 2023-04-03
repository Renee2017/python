class Student:


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self) -> str:
        return f"姓名:{self.name},年龄:{self.age}岁"
    
    def eat(self):
        print(f'{self.name}要吃饭')

    def sleep(self):
        print(f'{self.name}要睡觉')

    def year(self):
        self.age+=1      #此处修改了年龄属性，如果想要查看修改后结果，还需要打印一次

xiaoming=Student("小明",18)
print(xiaoming)
xiaoming.eat()
xiaoming.sleep()
xiaoming.year()
print(xiaoming)
xiaohong=Student("小红",17)
print(xiaohong)
xiaohong.eat()
xiaohong.sleep()
xiaohong.year()
print(xiaohong)


