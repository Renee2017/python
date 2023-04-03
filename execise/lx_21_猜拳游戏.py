# 猜拳游戏
#  自己出拳(石头(1)/剪刀(2)/布(3)) input (player)
# 2. 电脑随机出拳 (使用随机数模块(工具)完成) (computer)
# 3. 判断输赢
# 3.1 玩家胜利
# 3.1.1 player==1 and computer == 2
# or
# 3.1.2 player==2 and computer == 3
# or
# 3.1.3 player==3 and computer == 1
# 3.2 平局 player == computer
# 3.3 玩家输了 else


# 案例中需要电脑随机出拳,即随机出 1 2 3
# 在 Python 中想要随机获得整数数字可以使用如下方法
# # 1. 导入随机数工具包
# import random
# # 2. 使用工具包中的工具产生指定范围内的数字
# random.randint(a, b) # 产生[a, b] 之间的随机整数,包含 a b 的
import random
while True:
    # 注意转换类型
    player=int(input('玩家请出拳：石头1/剪刀2/布3/退出0\n'))
    computer=random.randint(1,3)
    if player==0:
        break
    if (player!=1) and(player!=2) and(player!=3):
        print('输入错误,player为 %d,类型为 %s' %(player,type(player)))
    else:
        if (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
            print('玩家赢')
        elif player==computer:
            print('平局')
        else:
            print('玩家输')