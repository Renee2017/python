def sum():
    num=0
    for i in range(1,101):
        if i%2==0:
            num=i+num
    print(num)
sum()