<?php
$servername="db";
$username="root";
$password="root";
$db="message";
$conn=mysqli_connect($servername, $username,$password,$db);
$message=$_POST["message"];
$sql="insert into updates (message)values('$message')";
$result=mysqli_query($conn,$sql);
echo "success:";
mysqli_close($conn);
header("Location: http://test/index.html");

?>
