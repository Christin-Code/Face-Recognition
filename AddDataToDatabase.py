import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facedetectiondatabase-7fe17-default-rtdb.firebaseio.com/"
})

ref = db.reference('Employees')

data = {
   "235417":
       {
           "Id": "235417",
           "name": "Christina Hart",
           "department": "Accounting",
           "joined_year": 2017,
           "total_attendance": 6,
           "standing": "G",
           "last_attendance_time": "2022-12-11 00:54:34"

       },
   "339855":
       {
           "Id": "339855",
           "name": "Virat",
           "department": "Managing",
           "joined_year": 2011,
           "total_attendance": 14,
           "standing": "E",
           "last_attendance_time": "2022-12-11 00:54:34"

       },
   "485748":
       {
           "Id": "485748",
           "name": "Dhoni",
           "department": "Accounting",
           "joined_year": 2015,
           "total_attendance": 12,
           "standing": "G",
           "last_attendance_time": "2022-12-11 00:54:34"

       }

}
for key,value in data.items():
   ref.child(key).set(value)








