import sys
from zipfile import ZipFile

if len(sys.argv) != 2:
    sys.exit("Usage: python3 zip.py <ZIP file>")

try:
    ZipFile(sys.argv[1], "r").printdir()
except FileNotFoundError:
    sys.exit("Error: File does not exist.")
