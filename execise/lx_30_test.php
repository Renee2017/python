
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
<form id="loginform" method="post">
                   <input type="text" value="" placeholder="手机号/邮箱" name="text1" id="text1" autocomplete="off">
                       
                            <input type="password" value="" placeholder="密码" name="pass1" id="pass1" autocomplete="off">
                        
                            <input type="text" value="" placeholder="验证码" name="verify_code" id="verify_code" autocomplete="off">
                             
                           <input type="submit" value="Submit">
<!--form表单如果没有action提交页面到本身-->
                     
</form>
		<?php 
if(!empty($_POST['text1'])){  
echo "post方式</br>";
$user =$_POST['text1'];
    $pass = $_POST['pass1'];
	echo "你post方式输入用户名是";
	echo ($user) ;
	echo "</br>";
	echo "你post方式输入密码是";
	echo ($pass) ;
}
else
{
echo "Get方式</br>";
$user =$_GET['text1'];
    $pass = $_GET['pass1'];
	echo "你Get方式输入用户名是";
	echo ($user) ;
	echo "</br>";
	echo "你Get方式输入密码是";
	echo ($pass) ;
}
	
?>
		
	</body>
</html>