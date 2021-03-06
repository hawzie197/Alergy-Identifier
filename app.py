# Author: Michael Hawes Tony Tran
# 2 March 2017

import os
import afflictionID
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg'])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello"

@app.route('/print/<filename>', methods = ['POST'])
def print_name(filename):
    return (open('C:/Users/tonyb/desktop/'+filename+'.txt','r').readline())
@app.route('/open/<filename>', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file2 = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file2 and allowed_file(image):
            filename = secure_filename(image)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #os.system('python /tf_files/label_image.py /images/'+filename+'>> '+filename+'.txt')
            #database stuff here
            #return 'snake'
    # '''return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''

    os.system('python /tf_files/label_image.py /tf_files/affliction/{}/{} > {}.txt'.format(animal, filename, filename))
    animal = open('/tf_files/affliction/{}/{}.txt '.format(animal, filename), 'r')
    #string = afflictionID.read_from_db(animal)
    print(animal)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
