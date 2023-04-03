# 定义一个游戏类 Game , 包含实例属性 玩家名字( name )
# 1. 要求记录游戏的最高分( top_score 类属性),
# 2. 定义方法: show_help 显示游戏的帮助信息 输出 这是游戏的帮助信息
# 3. 定义方法: show_top_score , 打印输出游戏的最高分
# 4. 定义方法: start_game , 开始游戏, 规则如下
# 1. 使用随机数获取本次游戏得分 范围 (10 - 100 )之间
# 2. 判断本次得分和最高分之间的关系
# 如果本次得分比最高分高,
# 修改最高分
# 如果分数小于等于最高分,则不操作
# 3. 输出本次游戏得分
import random


class Game:
    top_score=0
    top_score_player=0
    def __init__(self,name) -> None:
        self.name=name

    def show_help(self):
        print('这是游戏的帮助信息')

    def show_top_score(self):

        print(f"游戏的最高分为{Game.top_score},姓名：{Game.top_score_player}")

    def start_game(self):
        print(f'{self.name}现在开始玩游戏',end='')
        score=random.randint(10,100)
        print(f"，取得分数为{score}")
        if score> Game.top_score:
            Game.top_score=score
            Game.top_score_player=self.name


xiaowang=Game("小王")
xiaowang.start_game()
xiaowang.show_top_score()
xiaoli=Game("小李")
xiaoli.start_game()
xiaoli.show_top_score()
xiaoliu=Game("小刘")
xiaoliu.start_game()
xiaoliu.show_top_score()

xiaowang.show_help()

