class computer:


    def __init__(self,brand,price,movie_name) :
        self.brand=brand
        self.price=price
        self.movie_name=movie_name

    

    def __str__(self) -> str:  #用于打印时调用
        return f'{self.brand}电脑的价格为{self.price}元'
    
    def play_movie(self):
        print(f'{self.brand}播放电影{self.movie_name}')
        
mi=computer('mi',3600,'葫芦娃')
mi.play_movie()
print(mi)   
mac=computer("mac",2100,"变形金刚")
mac.play_movie()
print(mac)
computer.name=2     #设置类对象\类名的属性名
print(computer.name)   #查询你类对象\类名的属性名