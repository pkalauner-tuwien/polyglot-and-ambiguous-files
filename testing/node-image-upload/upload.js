const express = require("express");
const app = express();
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const os = require("os");
const crypto = require("crypto");
const imageType = require('image-type');
const jade = require("jade");
const { spawnSync } = require('child_process');
const { expressCspHeader, INLINE, NONE, SELF } = require('express-csp-header');
 
app.use(expressCspHeader({
    directives: {
        'default-src': [SELF]
    }
}));

const UPLOAD_DIRECTORY = "uploads";
const ABS_UPLOAD_DIRECTORY = path.join(__dirname, UPLOAD_DIRECTORY);
const ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "gif"];

app.set("views", path.join(__dirname, "templates"));
app.set("view engine", "jade");

const upload = multer({
    dest: os.tmpdir()
});

app.get(["/", "/upload"], (req, res) => {
    res.render("upload");
});

app.post("/upload", upload.single("file"), (req, res) => {
    if (!req.file) {
        res.render("upload", {
            msg: "No file selected."
        });
        return;
    }

    const tempPath = req.file.path;
    const filename = path.basename(req.file.originalname);
    const extension = path.extname(req.file.originalname).substring(1).toLowerCase();

    // Check extension
    if (!ALLOWED_EXTENSIONS.includes(extension)) {
        fs.unlink(tempPath, () => {
            res.render("upload", {
                msg: "The selected file has an invalid extension."
            });
        });
        return;
    }
    // Check file content so only changing extension cannot bypass the check
    fs.readFile(tempPath, (err, data) => {
        const type = imageType(data);
        if (type == null || !ALLOWED_EXTENSIONS.includes(type.ext)) {
            fs.unlink(tempPath, () => {
                res.render("upload", {
                    msg: "The selected file is not an image."
                });
            });
            return;
        }

        const hashedName = crypto.createHash('md5').update(filename).digest("hex");
        let targetPath = path.join(UPLOAD_DIRECTORY, hashedName + '.' + extension)

        // Append number if file already exists
        let id = 1;
        while (fs.existsSync(targetPath)) {
            targetPath = path.join(UPLOAD_DIRECTORY, hashedName + '_' + id++ + '.' + extension);
        }
        // Move target to uploads directory
        fs.rename(tempPath, targetPath, () => {
            res.render("upload", {
                msg: "Upload successful!",
                imagepath: targetPath
            });
        });
    });
});

app.get("/view", (req, res) => {
    let path = req.query.image;
    // Check if image exists
    if (!fs.existsSync(path)) {
        // Vulnerable, see method below
        res.send(jade.render("h4 Image " + path + " does not exit.", {
            exec_script: exec
        }));
    } else {
        res.render("view", {
            imagepath: path
        });
    }
});

// PoC method to show why attackers should not be able to upload arbitrary code.
// This method should obviously not exist in a real application, but code execution could also be achieved through other, more sophisticated ways.
function exec(file) {
    return spawnSync('node', [file]).stdout.toString();
}

app.get("/uploads/:filename", (req, res) => {
    res.sendFile(path.join(ABS_UPLOAD_DIRECTORY, req.params.filename));
});

app.listen(3000);
console.log("Running on localhost:3000");
