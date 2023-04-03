# 需求：1.小明体重75Kg  2.小明每次跑步会减肥0.5kg  3.小明每次吃东西体重会增加1kg
class person:
    def __init__(self,name,weight,time_run,time_eat):
        self.name= name
        self.weight=weight
        self.time_run=time_run
        self.time_eat=time_eat
    def __str__(self) -> str:
        return f'姓名为{self.name}，体重为{self.weight}kg'
    def run(self,time_run):
        self.weight-=0.5*time_run
        print(f'{self.name}跑了{time_run*5}千米，体重减少了{time_run*0.5}kg')
    def eat(self,time_eat):
        self.weight+=time_eat
        print(f'{self.name}吃了{time_eat}次，体重增加了{time_eat}kg')
               
stu=person('小明',75,1,1)
print(stu)
stu.run(2)
print(stu)
stu.eat(2)
print(stu)
    