import os
from os import path, walk
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
    destination = "/".join([target, 'input.jpg'])
    file.save(destination)

    # Use daltonize
    os.system("daltonize.py -s -t p static/input.jpg static/output.jpg")

    chosen_type = "Protanopia (Missing red cone)"
    
    # Renders the uploaded template, passes the file name that was assigned to the uploaded file and the chosen type
    return render_template("uploaded.html", chosen_type=chosen_type, input_filename='input.jpg', output_filename='output.jpg')

# Updates the uploaded.html template with the new select value and the updated output image
@app.route("/display/", methods=["POST"])
def display():
    type_value = request.form.get("types")
    os.system(f"daltonize.py -s -t {type_value} static/input.jpg static/output.jpg")
    print(type_value)

    if type_value == 'p':
        chosen_type = "Protanopia (Missing red cone)"
    elif type_value == 'd':
        chosen_type = "Deuteranopia (Missing green cone)"
    elif type_value == 't':
        chosen_type = "Tritanopia (Missing blue cone)"
    else:
        chosen_type = "Protanopia (Missing red cone)"

    return render_template("uploaded.html", chosen_type=chosen_type, input_filename='input.jpg', output_filename='output.jpg')

# Fix for the shift refresh issue where static does not update when render_template is used
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    print('cache changes applied')
    return response

if __name__ == "__main__":
    app.run()