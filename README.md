# Polyglot and ambiguous files

This repository contains various polyglot and ambiguous files created as part of my bachelor's thesis.

## Usage

This section describes which commands have to be executed to produce the files present in the `output` directory.

**Required libraries:**
- `createAmbiguousPDF.py`
    - `Pillow==7.0.0`
- `createAmbiguousGIF.py`
    - `imageio==2.8.0`

Run `pip install -r requirements.txt` to install all requirements at once. Note that `requirements.txt` also contains the requirements needed for the [testing environments](#testing-environments).

The working directory for the following commands should be `scripts`.

### Polyglots

PDF-ZIP

```
python3 appendFile.py ../input/PDF/hello.pdf ../input/ZIP/txt_files.zip ../output/pdf_zip.zip.pdf
python3 fixZIPOffsets.py ../output/pdf_zip.zip.pdf
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

GIF-JS

```
python3 appendFile.py files/gif_js_template.gif ../input/JS/hello.js ../output/gif_js.js.gif
```

PDF-ZIP (nested)

```
python3 createPDF_ZIP.py ../input/PDF/hello.pdf ../input/ZIP/txt_files.zip ../output/pdf_zip_nested.zip.pdf
```

JS-JAVA

```
python3 createJS_JAVA.py ../input/JS/hello.js ../input/JAVA/Hello.java ../output/Hello.java.html
```

JPEG-JS

```
python3 createJPEG_JS.py ../input/JPEG/hello.jpg ../input/JS/hello.js ../output/jpeg_js.js.jpg
```

JPEG-ZIP

```
python3 createJPEG_ZIP.py ../input/JPEG/hello.jpg ../input/ZIP/txt_files.zip ../output/jpeg_zip.zip.jpg
```

JPEG-PDF

```
python3 createJPEG_PDF.py ../input/JPEG/hello.jpg ../input/PDF/hello.pdf ../output/jpeg_pdf.pdf.jpg
```

SVG-JS

```
python3 createSVG_JS.py ../input/SVG/hello.svg ../input/JS/hello.js ../output/svg_js.svg
```

PDF-HTML

```
python3 createPDF_HTML.py ../input/PDF/hello.pdf ../input/HTML/hello.html ../output/pdf_html.html.pdf
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

GIF

```
python3 createAmbiguousGIF.py ../input/JPEG/red.jpg ../input/JPEG/green.jpg ../output/two_images.gif
```

ZIP

```
python3 createAmbiguousZIP.py ../input/TXT/file1.txt ../input/TXT/file2.txt ../input/TXT/file3.txt ../input/TXT/file4.txt ../output/four_zips.zip
```

## Testing environments

This section describes which commands have to be executed to start various applications for evaluation purposes.

### Simple image upload application

PHP

```
cd testing/php-image-upload/
php -S localhost:8080
```

Python (Flask)

```
cd testing/python-image-upload/
pip install flask flask-csp
export FLASK_APP=upload.py
flask run
```

Node.js

```
cd testing/node-image-upload/
npm install
node upload.js
```

### Show contents of ZIP

Java

```
cd testing/zip/
javac Zip.java
java Zip <ZIP-Archive>
```

Python

```
cd testing/zip/
python3 zip.py <ZIP-Archive>
```

PHP (requires `php-zip`)

```
cd testing/zip/
php zip.php <ZIP-Archive>
```
