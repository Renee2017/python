import random
while True:
    player=int(input("请出拳:石头1/剪刀2/布3/退出游戏0:"))
    if player==0:
        break
    elif player>3:
        print("输入错误，请重新输入")
    computer= random.randint(1,3)
    print(f"电脑：{computer}")
    print("电脑 {}".format(computer))
    print("电脑 %d"% computer)
    if (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
        print('玩家赢')
    elif player==computer:
        print('平局')
    else:
        print('再来一次吧')