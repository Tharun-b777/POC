<?php
$servername="localhost";
$username="root";
$password="root";
$db="message";
$conn=mysqli_connect($servername, $username,$password,$db);
$message=$_POST["message"];
$sql="insert into updates (receiver_id,message)values(2,'$message')";
$result=mysqli_query($conn,$sql);

mysqli_close($conn);
header("Location: http://test/index.html");

?>
