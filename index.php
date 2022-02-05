<?php
error_reporting(E_ERROR);
if($_GET['q']!=='')
{
$con=mysql_connect('localhost','root','');
$db=mysql_select_db('search');
?>
<html>
<head>
<script type="script/javascript">
function active()
{
	var sb=document.getElementById('searchBox');
	if(sb.value=='search..')
	{
		sb.value='';
		sb.placeholder='search...';
		
	}
	
}


function inactive()
{
	var sb=document.getElementById('searchBox');
	if(sb.value=='')
	{
		sb.placeholder='';
		sb.value='search...';
		
	}
}
</script>
<style text="style/css">
#searchBox
{
	border:1px solid #000000;
	border-right:none;
	-webkit-border-top-left-radius:10px;
	-webkit-border-bottom-left-radius:10px;
	-moz-border-radius-topleft:10px;
	-moz-border-radius-bottomleft:10px;
	border-top-left-radius:10px;
	border-bottom-left-radius:10px;
	font-size:16px;
	padding:10px;
	outline:none;
	width:250px;
}

#searchButton
{
	border:1px solid #000000;
	-webkit-border-top-right-radius:10px;
	-webkit-border-bottom-right-radius:10px;
	-moz-border-radius-topright:10px;
	-moz-border-radius-bottomright:10px;
	border-top-right-radius:10px;
	border-bottom-right-radius:10px;
	font-size:16px;
	padding:10px;
	background:#f1d829;
	font-weight:bold;
	cursor:pointer;
	outline:none;
	margin-left:-4px;
}

#searchButton:hover
{
	background:blue;
}
body
{
	font-family:arial;
}
h3
{
	margin:20px 0px 0px 0px;
	padding:0;
}
p
{
	margin:0px;
	padding:0px;
}
a:hover
{
	text-decoration:none;
}
#hello
{
	margin-left:510px;
	margin-top:50px;
}

</style>
</head>
<body>
<div id=hello>
<?php
/* $e=date("d-m-Y");
$d=new datetime('2018-09-07 07:27:10');
$d->modify('+1 day');
if(($e==$d->format('d-m-Y')))
*/
$b=array("a.JPG","b.PNG","c.JPG","d.PNG","e.JPG","f.JPG","g.JPG","h.JPG","i.JPG","j.JPG");
$a=rand(0,9);
{
	echo "<img src='$b[$a]' height=200px, width=300px >";
}
/*else
{
	echo "<img src='j.jpg' height=200px, width=300px >";
}
*/
?>
<br/><br/><br/><br/>
<form  action="index.php" method="GET" id="searchform" />

<input type="text" name="q" id="searchBox" placeholder="search here" value="" maxlength="25" autocomplete="off" />
<input type="submit" id="searchButton"  value="submit" />
</form>
</div>
<?php
$hello=$_GET['q'];
if(!isset($_GET['q']))
{
	echo '';
}
else
{
$query=mysql_query("select * from product where title LIKE '%$hello%' OR description LIKE '%$hello%'");
$num_row=mysql_num_rows($query);
?>
<p><strong><?php echo $num_row;?></strong>results for '<?php echo $hello; ?>'</p>
<?php
while($row=mysql_fetch_array($query))
{
	$id=$row['id'];
	$title=$row['title'];
	$description=$row['description'];
	
	echo '<h3><a href="'.$id.'.php">'.$title. '</a></h3><p>Branded by:-'.$description.'</p><br />';
	
}
}
?>
</body>
</html>
<?php
}
else
{
	header('Location:test.php');
}
?>