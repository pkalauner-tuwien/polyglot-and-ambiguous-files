<?php
    if (count($argv) != 2) {
        die("Usage: php zip.php <ZIP file>\n");
    }
    if (!class_exists("ZipArchive")) {
        die("Error: php-zip is not installed.\n");
    }

    $za = new ZipArchive();
    if ($za->open($argv[1]) != 1) {
    	die("Error: File could not be opened.\n");
    }
    for ($i = 0; $i < $za->numFiles; $i++) {
        echo($za->statIndex($i)["name"] . "\n");
    }
?>
