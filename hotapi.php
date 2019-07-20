<?php
error_reporting( E_ALL&~E_NOTICE );
header('Content-type: application/json');

//获取请求栏目
$item = $_GET['item'];
if($item=="zhihu"){
    $fname = "json/zhihu.json";
}
elseif($item=="baidurd"){
    $fname = "json/baidurd.json";
}
elseif($item=="baidusj"){
    $fname = "json/baidusj.json";
}
elseif($item=="vsite"){
    $fname = "json/vsite.json";
}
elseif($item=="tieba"){
    $fname = "json/tieba.json";
}
elseif($item=="weibo"){
    $fname = "json/weibo.json";
}
else{
    $fname = "json/weibo.json";
}
post_data($fname);
function post_data($filename){
    //获取回调函数名
    $jsoncallback = htmlspecialchars($_REQUEST ['jsoncallback']);
    $handle = fopen($filename, "r");
    //通过filesize获得文件大小，将整个文件一下子读到一个字符串中
    $contents = fread($handle, filesize ($filename));
    //将上面的字符串分割成数组，分隔符号为逗号。
    $pieces = explode(",", $contents);
    $new_data="";
    for($i=0;$i<20;$i++){
        $new_data = $new_data . $pieces[$i].',';
    }
    //拼接字符串
    $new_data = $jsoncallback ."(" .'[' . $new_data . "\n" . ']'. ")" ;
    echo $new_data;
    fclose($handle);
}

?>