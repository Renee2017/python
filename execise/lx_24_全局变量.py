
num=(2,4)
print(num)
def c():
    global num
    num=(9,0)
    return num
c()
print(num)
