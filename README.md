# Polyglot and ambiguous files

This repository contains various polyglot and ambiguous files created as part of my bachelor's thesis.

## Usage

This section describes which commands have to be executed to produce the files present in the `output` directory.

**Required libraries:**
- `createAmbiguousPDF.py`
    - `Pillow==7.0.0`

Run `pip install -r requirements.txt` to install all requirements at once. Note that `requirements.txt` also contains the requirements needed for the [testing environments](#testing-environments).

The working directory for the following commands should be `scripts`.

### Polyglots

PDF-ZIP

```
python3 appendFile.py ../input/PDF/hello.pdf ../input/ZIP/txt_files.zip ../output/pdf_zip.zip.pdf
```

ZIP-PDF

```
python3 appendFile.py ../input/ZIP/txt_files.zip ../input/PDF/hello.pdf ../output/zip_pdf.pdf.zip
```

PDF-JAR

```
python3 appendFile.py ../input/PDF/hello.pdf ../input/JAR/hello.jar ../output/pdf_jar.jar.pdf
```

GIF-PHP

```
python3 appendFile.py ../input/GIF/hello.gif ../input/PHP/hello.php ../output/gif_php.php.gif
```

JS-JAVA

```
python3 createJS_JAVA.py ../input/JS/alert.js ../input/JAVA/Hello.java ../output/Hello.java.html
```

SVG-JS

```
python3 createSVG_JS.py ../input/SVG/hello.svg ../input/JS/alert.js ../output/svg_js.svg
```

### Ambiguous files

PDF (two images in one PDF)

```
python3 createAmbiguousPDF.py ../input/JPEG/red.jpg ../input/JPEG/green.jpg ../output/two_images.pdf
```

PDF (three images in one PDF)

```
python3 createAmbiguousPDF.py ../input/JPEG/red.jpg ../input/JPEG/green.jpg ../input/JPEG/blue.jpg ../output/three_images.pdf
```

ZIP

```
python3 createAmbiguousZIP.py ../input/TXT/file1.txt ../input/TXT/file2.txt ../input/TXT/file3.txt ../input/TXT/file4.txt ../output/four_zips.zip
```

## Testing environments

### PHP image upload

```
cd testing/php-image-upload
php -S localhost:8080
```

### Python image upload (Flask)

```
cd testing/python-image-upload
pip install flask
export FLASK_APP=upload.py
flask run
```
