import tools
class cat(tools.animal):
    def play(self):
        super().play()
        print('玩累了，等待铲屎官的投喂中')
miao=cat('小黄',3)
miao.play()