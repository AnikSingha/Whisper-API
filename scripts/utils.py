from flask import send_file
import os

def getOutputFolder():
    return os.getcwd() + "/outputs/"

def getUploadFolder():
    return os.getcwd() + "/uploads/"

def getSRTPath():
    return os.getcwd()+"/outputs/output.srt"

def emptyFolder(folder_path):
    contents = os.listdir(folder_path)
    for item in contents:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            if item != "readme.txt": 
                os.remove(item_path)

        elif os.path.isdir(item_path):
            os.rmdir(item_path)

def cleanFolders():
    emptyFolder(getOutputFolder())
    emptyFolder(getUploadFolder()) 