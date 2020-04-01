<?php
    // Set CSP Header
    if(!headers_sent()) {
        header("Content-Security-Policy: default-src 'self'");
        header("X-Content-Security-Policy: default-src 'self'");
        header("X-WebKit-CSP: default-src 'self'");
    }
 ?>
 