import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    # Renders the index.html file
    return render_template("index.html")

@app.route("/upload/", methods=["POST", "GET"])
def upload():
    # Sets the target path for the file to be added to
    target = os.path.join(APP_ROOT, 'static')
    print(target)

    # Creates the path in case it doesn't exist
    if not os.path.isdir(target):
        os.mkdir(target)

    # Finding files in the requests, adding them to the target destination with the name as their filename
    file = request.files["file"]
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)
    
    # Gets the selection from the select in uploaded.html
    chosen_type = request.form.get("types")
    
    # Renders the uploaded template, passes the file name that was assigned to the uploaded file and the chosen type
    return render_template("uploaded.html", image_name=filename, chosen_type=chosen_type)

# This isn't finished but I think the uploaded.html file will need to run this as an action when the select form is changed? And then somehow it passes the original image as well as the new outputed corrected image
@app.route("/display/", methods=["POST", "GET"])
def display():
    return render_template("uploaded.html", image_name=filename, chosen_type=chosen_type)

if __name__ == "__main__":
    app.run()