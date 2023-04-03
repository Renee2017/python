<?php
//_GET、_POST、_FILE等格式的全是系统定义的变量。
//接口文档里说：往接口http://192.168.2.174/bot/post.php
//用Get 方式提交数据，数据为 password=Qq2017..
//eg:http://192.168.2.174/bot/post.php?user=admin&password=Qq2017..

if(isset($_POST["password"])&&!empty($_POST["password"]))   //判断有没有post提交password参数 且 不为空

//判断_GET里存在report，且report的值不为false。
//不能用一个不存在的东西，所以先用isset()判定存不存在,存在了再使用
// python：and or 
// c&php ：&&  ||
{	
	// echo "你输入的password是：";
	// echo $_POST["password"];
	// echo "</br>";
	 //能跑到这里，肯定有post提交password参数
	if($_POST["verify_code"]=="8888") 
	{
		if(
			($_POST["username"]=="18002612856")  && 
			($_POST["password"]=="Qq2017..")
			) //判断提交的password值是不是Qq2017..
		{
			//echo "login ok";
			//提交的password值肯定是Qq2017..
			echo try_json_encode("200","login ok");#php中每次echo出来的都是html格式的代码
			exit(); #确保echo之后就结束整个文件代码，后面的form表单不会再出现

		}
		else
		{
			//提交的password值或username值不对
			echo try_json_encode("403","login fail");
			exit();

			//调用try_json_encode 进行 try json encode
		}
	}
	else
	{
		echo try_json_encode("401","verify_code failed");
		exit();
	}
}
else
{
	//能跑到这里，肯定没有post提交password参数
	echo try_json_encode("401","no password");
	exit();
	//调用try_json_encode 进行 try json encode
}


function try_json_encode($retcode_temp,$message_temp){
	$before=array("retcode"=>$retcode_temp,"message"=>$message_temp);  
    //创建数组，在数组内装入$retcode_temp,$message_temp的值，并把赋值完的数组赋值给变量before。
	$after=json_encode($before);
	//把数组before传给json_encode函数，顾名思义，这个函数会把数组编码成json格式并返回，返回值赋值给after变量。
	return $after;
	//编码完的json返回
}
?>

<!--下面是html格式-->
<form id="loginform" method="post">
	<input type="text" value="" placeholder="手机号/邮箱" name="username" id="text1" autocomplete="off">
		
	<input type="password" value="" placeholder="密码" name="password" id="pass" autocomplete="off">

	<input type="text" value="" placeholder="验证码" name="verify_code" id="verify_code" autocomplete="off">
		
	<input type="submit" value="Submit">
<!--form表单如果没有action提交页面到本身-->
                     
</form>
