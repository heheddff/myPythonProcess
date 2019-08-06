<?php
require_once("./session.php");
?>
<!doctype html>
  <head>
    <title>Serverlist</title>
    <!--<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">-->
    <link rel="stylesheet" href="./css/static/bootstrap.min.css">
    <link rel="stylesheet" href="./css/static/./icon/iconfont.css">
    <script type=text/javascript src="./css/static/jquery-1.7.1.min.js"></script>
    <script type=text/javascript src="./css/static/icon/iconfont.js"></script>
    <style>
    .icon {
      width: 1em;
      height: 1em;
      vertical-align: -0.15em;
      fill: currentColor;
      overflow: hidden;
    }
    a:hover{
        text-decoration: none;
    }
    .start{
        color:#006569;
    }
    .stop{
        color:#333333;
    }
    .restart{
        color:#B77674;
    }
    .layout{
        position:absolute;
        left:0;
        top:0;
        width:100%;
        height:100%;
        background:rgba(0,0,0,0.5);
        z-index:100;
    }
    </style>
  </head>

<body>
  <div class="container-fluid">
      <button id="allSelect" type="button" class="btn btn-primary">全选/反选</button>
        <a class="btn btn-primary" data="1">Start</a>
        <a class="btn btn-warning" data="2">Stop</a>
        <!--<a class="btn btn-info" data="3">Restart</a>-->
    <div class="row">
      <?php
        header('Access-Control-Allow-Origin:*');
        $posts = file_get_contents('http://127.0.0.1:5002/?api=php');
        $posts = json_decode($posts,TRUE);
        foreach ($posts as $post=>$v){
            echo '<div class="col-2 border border-primary rounded m-1 p-1">';
            if ($v == 1){
                $cs = "text-success";
                $res = "已启动";        
            }
            elseif ($v == 2) {
                $cs = "text-muted";
                $res = "未启动";
            }
            elseif ($v == 3) {
                $cs = "text-danger";
                $res = "异常";
            }
            echo '<p id='.$post.'><input type=checkbox>&nbsp;'.$post.'
                
                <a href=# data=1 title=启动 class="iconfont icon-start start"></a>
                <a href=# data=2 title=关闭 class="iconfont icon-guanbi stop"></a>
                
            <br>
                当前状态:<span id="result" class="'.$cs.'">'.$res.'</span>
             </p>';
            
            /* 
             * <a href=# data=3 title=重启 class="iconfont icon-zhongqi restart"></a>
            echo '
            <p id='.$post.'><input type=checkbox>&nbsp;'.$post.'
                <svg class="icon svg-icon" aria-hidden="true" data=1 title=启动>
                    <use xlink:href="#icon-start"></use>
                </svg>
                <svg class="icon svg-icon" aria-hidden="true"  data="2" title="关闭">
                     <use xlink:href="#icon-guanbi"></use>
                </svg>
                 <svg class="icon svg-icon" aria-hidden="true"  data="3" title="重启">
                    <use xlink:href="#icon-zhongqi"></use>
                 </svg>
            <br>
                当前状态:<span id="result" class="'.$cs.'">'.$res.'</span>
             </p>';*/
       echo '<div ></div></div>';
       #echo '<div class="layout"></div>';
        }
       ?>     
    </div>
  </div>

<script>
/*
$("svg").click(function() {
    ser_id= $(this).parent().attr('id')
    stype= $(this).attr('data')
    span = $(this).parent().find('span')
    console.log($(this).parent().attr('id'))
    console.log(stype)
    ajaxPost(ser_id,stype,span)

});*/

$("a.iconfont").click(function() {
    ser_id= $(this).parent().attr('id')
    stype= $(this).attr('data')
    span = $(this).parent().find('span')
    layout = $(this).parent().parent().find('div').last()
    
    console.log($(this).parent().parent().find('div').last().text())
    console.log($(this).parent().attr('id'))
    console.log(stype)
    ajaxPost(ser_id,stype,span,layout)

});

function ajaxPost(ser_id,stype,span,layout){
    result = {1:'已启动',2:'未启动',3:'异常',4:'Error'}
    cs = {1:'text-success',2:'text-muted',3:'text-danger',4:'text-danger'}
    waitinfo = {1:'正在启动...',2:'正在关闭...',3:'正在重启...'}
    data = { serid:ser_id, stype:stype}
    //ajax
    $.ajax({
        //增加遮罩层，防止多次提交
        beforeSend: function () {
            //alert('12333')
            span.attr('class','text-info')
            span.text(waitinfo[stype])
            layout.addClass('layout')
            //silent || $(this).trigger("ICC_AjaxStart", [requestId]);
            //$(this).trigger("ICC_AjaxBeforeSend", [requestId]);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            //alert(jqXHR)
            layout.removeClass('layout')
            console.log(jqXHR)
            console.log(textStatus)
            console.log(errorThrown)
        },
        data: data,
        dataType: "json",
        method: "post",
        global:false,
        crossDomain: true,
        success: function (res, textStatus) {
            console.log(res)
            //$(this).trigger("ICC_AjaxSuccess", [requestId, textStatus, res]);
            status = res.result[ser_id];
            //status = data.result[ser_id]
            span.attr('class',cs[status])
            span.text(result[status])
            layout.removeClass('layout')
            console.log(res)
            console.log(cs[status])
            console.log(result[status])
        },
        url: './api.php'
    })
}

//全选
    type = false
    $("#allSelect").click(function () {
        type = !type
        $("input[type='checkbox']").prop("checked", type);
    })

    $("a.btn").click(function () {
        inputs = $("input:checked")
        stype= $(this).attr('data')
        if (inputs.length > 0){
            console.log(inputs)
            inputs.each(function () {
                ser_id= $(this).parent().attr('id')

                span = $(this).parent().find('span')
                layout = $(this).parent().parent().find('div').last()
                
                console.log($(this).parent().attr('id'))
                console.log(stype)
                ajaxPost(ser_id,stype,span,layout)
            })
        }else{
            alert('please choose server!')
        }

    })
    </script>
    
</body>


