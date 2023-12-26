from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from scripts.transcribe import createSRTFile
from scripts.utils import getUploadFolder, getOutputFolder, cleanFolders
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/')
def home():
    return "<h1>Hello Whisper</h1>", 200

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(getUploadFolder() + filename)
 
    outName = filename.split('.')[0] + '.srt'

    createSRTFile(getUploadFolder()+filename, model, outName)
    
    return send_file(getOutputFolder()+ outName, as_attachment=False), 200

@app.route('/clean', methods=['GET'])
def delete():
    cleanFolders()
    return "Successfully deleted all files", 200


