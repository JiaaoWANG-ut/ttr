
<h1>Liquid Electrolyte Database v0.1 Beta</h1>

<?php
$dbhost = '3.129.67.14';  // mysql服务器主机地址
$dbuser = 'root';            // mysql用户名
$dbpass = 'wja001';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('连接失败: ' . mysqli_error($conn));
}
// 设置编码，防止中文乱码
mysqli_query($conn , "set names utf8");

$sql = 'SELECT runoob_id, runoob_title, 
        runoob_author, submission_date
        FROM runoob_tbl';

mysqli_select_db( $conn, 'test_0' );
$retval = mysqli_query( $conn, $sql );
if(! $retval )
{
    die('无法读取数据: ' . mysqli_error($conn));
}
echo '<h2>Sorry, you do not have access</h2>';
echo '<table border="1"><tr><td> ID</td><td>Example</td><td>Author</td><td>Submit Date</td></tr>';
while($row = mysqli_fetch_array($retval, MYSQLI_ASSOC))
{
    echo "<tr><td> {$row['runoob_id']}</td> ".
         "<td>{$row['runoob_title']} </td> ".
         "<td>{$row['runoob_author']} </td> ".
         "<td>{$row['submission_date']} </td> ".
         "</tr>";
}
echo '</table>';
mysqli_close($conn);
?>

