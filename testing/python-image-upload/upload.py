from flask import *
from flask_csp.csp import csp_header, csp_default
import imghdr
import os
import hashlib
import subprocess

app = Flask(__name__)

app.config["UPLOAD_DIRECTORY"] = 'uploads'
app.config["ALLOWED_EXTENSIONS"] = ["jpg", "jpeg", "png", "gif"]

# Remove report-uri from default CSP header
h = csp_default()
h.update({'report-uri':""})

@app.route('/')
@app.route('/upload')
@csp_header()
def index():  
    return render_template("upload.html")

@app.route('/upload', methods = ['POST'])
@csp_header()  
def upload():
    f = request.files['file']
    # Check extension
    if not "." in f.filename:
        return render_template("upload.html", msg="The selected file has an invalid extension.")

    name, ext = f.filename.rsplit(".", 1)
    ext = ext.lower()
    if ext not in app.config["ALLOWED_EXTENSIONS"]:
        return render_template("upload.html", msg="The selected file has an invalid extension.")
    
    hashed_name = hashlib.md5(name.encode("utf-8")).hexdigest()
    path = os.path.join(app.config["UPLOAD_DIRECTORY"], "{}.{}".format(hashed_name, ext))

    # Append number if file already exists
    id = 1
    while os.path.isfile(path):
        path = os.path.join(app.config["UPLOAD_DIRECTORY"], "{}_{}.{}".format(hashed_name, id, ext))
        id += 1

    f.save(path)

    # Check file content so only changing extension cannot bypass the check
    if imghdr.what(path).lower() not in app.config["ALLOWED_EXTENSIONS"]:
        os.remove(path)
        return render_template("upload.html", msg="The selected file is not an image.")
    
    return render_template("upload.html", msg="Upload successful!", imagepath = path)

@app.route('/view')
@csp_header()
def view():
    imagepath = request.args.get('image')
    if not os.path.isfile(imagepath):
        # Vulnerable, see method below
        template = "{% extends 'index.html' %}{% block content %}<h4>Image " + imagepath + " does not exist.</h4>{% endblock %}"
        return render_template_string(template)
        
    return render_template("view.html", imagepath=imagepath)

# PoC method to show why attackers should not be able to upload arbitrary code.
# This method should obviously not exist in a real application, but code execution could also be achieved through other, more sophisticated ways.
def exec_script(file):
	return subprocess.check_output(['python3', file])
app.jinja_env.globals['exec_script'] = exec_script # Allow usage in templates

@app.route('/uploads/<filename>')
@csp_header()
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_DIRECTORY"], filename)
