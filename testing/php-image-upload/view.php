<?php
    include("csp_header.php");
 ?>
<p><a href="index.php">Upload another image</a></p>
<?php
    $imagepath = $_GET["image"]; 
    if (!file_exists($imagepath)) {
        echo "<h4>Image $imagepath does not exist.</h4>";
    } else {
        echo "<img src='$imagepath'>";
    }
?>
