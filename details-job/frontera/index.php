<!DOCTYPE html>
<html>
<body>
<h1>Supercomputer Online Monitoring</h1>
<h2>JiaaoWang@Henkelman Group, UT Austin, wangjiaao0720@utexas.edu</h2>

<a class="hxex" href="../">BACK</a>

<div>Supercomputer JOB Monitor</div>
<hr />

<body>

  <div class="container-fluid">
  <h3 class="text-center mt-3">TACC Frontera </h3>
  <h5 class="text-center">Welcome to Supercomputer JOB Mannagement Center</h5>
             


<?php
  $output = exec("python3 server-command.py 2>&1", $result, $status);
    if ($status === 0) {
	    echo implode("\n", $result);
	    #echo "  The current time in CST is: " . date("Y-m-d h:i:s A", time() + 3600 * 6);

  } else {
    echo "Error: $output";
  }

   # echo "The current time in CST is: " . date("Y-m-d H:i:s", time() + 3600 * 6);
?>

<?php

$file = fopen("temp", "r");




  echo "<pre>";
  while (!feof($file)) {
    $line = fgets($file);
    $elements = preg_split("/\s+/", $line);
    foreach ($elements as $element) {
      printf("%15s", $element);
    }
    echo "\n";
  }
  echo "</pre>";
  fclose($file);



?>



