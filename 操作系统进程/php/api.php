<?php

header('Access-Control-Allow-Origin',"*");

$url = "http://127.0.0.1:5002/add?serid=".$_REQUEST['serid']."&stype=".$_REQUEST['stype'];

echo file_get_contents($url);

