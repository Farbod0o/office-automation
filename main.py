from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from controller.controller import Controller
app = Flask(__name__, template_folder='view/templates',static_folder='view/statics')
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-dep', methods=['POST'])
def submit_dep_form():
    print("hi")
    name = request.form.get('name')
    phone = request.form.get('phone')
    department_num = request.form.get('department-num')
    short_description = request.form.get('short-description')
    additional_description = request.form.get('additional-description')

    photo = request.files['photo']
    if photo:
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        photo.save(photo_path)
    status,dep = Controller.add_department(name,1,photo_path,short_description,"address",phone,additional_description)
    if status:
        return jsonify({"status": status, })
    else:
        return jsonify({"status": status,"message":dep})


if __name__ == '__main__':
    app.run(debug=True)
