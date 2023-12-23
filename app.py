from flask import Flask, request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/uploads"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return str(type(file))

if __name__ == '__main__':
    app.run()

#curl -X POST -H "Content-Type: multipart/form-data" -F "file=@C:\Users\aniks\Downloads\programming\x.mp4" http://127.0.0.1:5000/upload