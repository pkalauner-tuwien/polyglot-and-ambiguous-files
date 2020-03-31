<form action="index.php?site=upload.php" method="post" enctype="multipart/form-data">
    <label for="inputFile">Choose file: </label>
    <input type="file" name="file" id="inputFile">
    <br>
    <button type="submit">Submit</button>
</form>
<?php
	if (isset($_FILES["file"])) {
		$upload_dir = 'uploads/';
		$filename = md5(pathinfo($_FILES['file']['name'], PATHINFO_FILENAME));
		$extension = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));
		
		// Check file extension
		$allowed_extensions = array('jpg', 'jpeg', 'png', 'gif');
		if (!in_array($extension, $allowed_extensions)) {
			echo "The selected file has an invalid extension.";
			return;
		}
		
		// Check file content so only changing extension cannot bypass the check
		$allowed_types = array(IMAGETYPE_JPEG, IMAGETYPE_PNG, IMAGETYPE_GIF);
		$detected_type = exif_imagetype($_FILES['file']['tmp_name']);

		if (!in_array($detected_type, $allowed_types)) {
			echo "The selected file is not an image.";
			return;
		}

		$new_path = $upload_dir . $filename . '.' . $extension;
		// Append number if file already exists
		$id = 1;
		while (file_exists($new_path)) {
			$new_path = $upload_dir . $filename . '_' . $id++ . '.' . $extension;
		}
		
		// Create upload directory if it doesn't exist yet
		if (!file_exists($upload_dir)) {
			mkdir($upload_dir, 0777);
		}
		
		// Move file to upload directory
		move_uploaded_file($_FILES['file']['tmp_name'], $new_path);
		echo "Upload successful!<br><a href='index.php?site=view.php&image=$new_path'>Go to uploaded image</a>";
	}
?>
