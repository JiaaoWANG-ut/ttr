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
  <h3 class="text-center mt-3">High Throughput JOB Sequence</h3>
  <h5 class="text-center">Welcome to Supercomputer JOB Mannagement Center</h5>
    <?php
    // Enter your Directry/Folder Name I have Given Folder Name As Images
      $files = scandir('../images/');
      echo "<div class='row'>";
      foreach ($files as $file) {
        if ($file !== "." && $file !== "..") {
		// Give Image source -- src='folder-name/$file'
		echo "<div class=' col-6 col-sm-4 col-md-3 mt-3 mb-3'>

			<hr />
                <img src='../images/$file' alt='image' /></div>";
        }
      }
      echo "</div>";
    ?>
  </div>

</body>
</html>
