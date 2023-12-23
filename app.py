from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from scripts.transcribe import createSRTFile
from scripts.utils import getUploadFolder, getOutputFolder
import whisper

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = getUploadFolder()

model = whisper.load_model("base")

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(getUploadFolder() + filename)

    outName = filename.split('.')[0] + '.srt'

    createSRTFile(getUploadFolder()+filename, model, outName)
    
    return send_file(getOutputFolder()+ outName, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)

#curl -X POST -H "Content-Type: multipart/form-data" -F "file=@C:\Users\aniks\Downloads\x.mp4" http://127.0.0.1:5000/upload