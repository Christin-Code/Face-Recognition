import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facedetectiondatabase-7fe17-default-rtdb.firebaseio.com/",
    'storageBucket': "facedetectiondatabase-7fe17.appspot.com"
})



# Importing employee images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
employeeIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    employeeIds.append(os.path.splitext(path)[0])


    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)




    # print(path)
    # print(os.path.splitext(path)[0])
print(employeeIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)


    return encodeList



print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, employeeIds]
print("Encoding Complete")


file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")


