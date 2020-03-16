# Polyglot and ambiguous files

This repository contains various polyglot and ambiguous files created as part of my bachelor's thesis.

## Usage

### Polyglots

SVG-JS

```
python3 createSVG_JS.py ../input/SVG/hello.svg ../input/JS/alert.js ../output/svg_js.svg
```

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

JS-JAVA

```
python3 createJS_JAVA.py ../input/JS/alert.js ../input/JAVA/Hello.java ../output/Hello.java.html
```
