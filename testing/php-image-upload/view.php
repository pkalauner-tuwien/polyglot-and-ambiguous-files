<p><a href="index.php">Upload another image</a></p>
<?php
    echo "<img style='border: 2px solid black; max-width:60%;' src='" . htmlspecialchars($_GET["image"]) . "'>";
?>
