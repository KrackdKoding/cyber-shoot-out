<html>
<head>
    <meta http-equiv="refresh" content="10">
	<title>Cyber Shoot'em</title>

	<!-- links to the CSS stylesheet that makes the page pretty-->
	<link rel="stylesheet" type="text/css" href="css/style.css">

	<!--makes the website scale to the browser, so this is good for mobile browsers-->
	<meta name="viewport" content="width=device width, initial-scale=1.0">

</head>


<body>

<div class="title">Cyber Shoot'em</div>

<br>

<div class="title2">Recent Scores</div>
<table class="blueTable"> <!-- class should change -->
    <thead>
    <tr><th>Name</th><th>Score</th><th></th><th>Name</th><th>Score</th></tr>
    </thead>

<!-- php code that pulls from the database-->
<?php
$db = new SQLite3('/var/www/html/cyber/score.db') or die('Unable to open database');
$result1 = $db->query('SELECT * FROM scores WHERE device="a1" ORDER BY id DESC LIMIT 1') or die('Query failed');
$result2 = $db->query('SELECT * FROM scores WHERE device="a2" ORDER BY id DESC LIMIT 1') or die('Query failed');

while ($row = $result1->fetchArray())
{
    echo "<tr><td>";
    echo $row['name'];
    echo "</td><td>";
    echo $row['score'];
    echo "</td><td>";
}
while ($row = $result2->fetchArray())
{
    echo "</td><td>";
    echo $row['name'];
    echo "</td><td>";
    echo $row['score'];
    echo "</td></tr>";
}
?>
</tbody>
</table>

<br>
<div class="title2">High Scores</div>
<table class="blueTable">
	<thead>
	<tr><th>Name</th><th>Score</th></tr>
	</thead>

<!-- php code that pulls the data from the database-->
<?php

/*connects to the database*/
$database = new SQLite3('/var/www/html/cyber/score.db') or die('Unable to open database');
/*fills the result variable with a query that pulls the last 20 entries from the database*/
$result = $database->query('SELECT * FROM Scores ORDER by score DESC, ts DESC LIMIT 20') or die('Query failed');

/*this loop builds each row for the data in the results variable*/
while  ($row = $result->fetchArray())
{
	echo "<tr><td>";
	echo $row['name'];
	echo "</td><td>";
	echo $row['score'];
	echo "</td></tr>";

}
?>
</tbody>
</table>

</body>
</html>