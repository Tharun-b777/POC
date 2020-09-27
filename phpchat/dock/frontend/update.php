<?php
$servername="db";
$username="root";
$password="root";
$db="message";
$output="<br>";
$conn=mysqli_connect($servername, $username,$password,$db);

$sql="Select message from updates";
$result=mysqli_query($conn,$sql);
while($row=mysqli_fetch_assoc($result))
{
    if  (!empty($row["message"]))
{    $output.=$row["message"]."<br>";
}}
echo $output;
?>
