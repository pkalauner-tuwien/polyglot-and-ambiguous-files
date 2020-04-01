<?php
    include("csp_header.php");
 ?>
<html>
<head>
    <title>Image Upload</title>
</head>
<body>
    <h3>This simple web app represents a simple PHP image upload application which uses include.</h3>
    <?php
        $site = $_GET["site"];
        if (!isset($site)) {
            $site = "upload.php";
        }
        if (file_exists($site)) {
            include($site);
        } else {
            echo htmlspecialchars($site) . " not found.";
        }
    ?>
</body>
</html>
