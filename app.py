import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    """Landing page. Has an image upload button."""
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Page displayed after an image is uploaded. Currently it just displays the image and has a button to go back to the landing page."""
    target = os.path.join(APP_ROOT, 'static')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return render_template("uploaded.html", image_name=filename)



if __name__ == "__main__":
    app.run()