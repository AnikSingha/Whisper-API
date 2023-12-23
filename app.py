from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from transcribe import createSRTFile
import whisper
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/uploads"

model = whisper.load_model("base")

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    createSRTFile(os.getcwd()+"/uploads/"+filename, model)

    return send_file(os.getcwd()+"\\output.srt", as_attachment=False)

if __name__ == '__main__':
    app.run()

#curl -X POST -H "Content-Type: multipart/form-data" -F "file=@C:\Users\aniks\Downloads\programming\x.mp4" http://127.0.0.1:5000/upload