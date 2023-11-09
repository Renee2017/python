username="admin"
code ="123456"
verify='8888'
username1=input('请输入用户名')
code1=input('请输入密码')
verify1=input('请输入验证码')
if verify1==verify:
    print('验证码正确')
    if username1==username:
        print('用户名正确')
        if code1==code:
            print('密码正确，登录成功')
        else:
            print('密码错误，请重新输入')
    else:
        print('用户名错误，请重新输入')   
else:
    print('验证码不正确，请重新输入')

 