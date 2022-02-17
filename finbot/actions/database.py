import pyrebase as pyrebase

class Firebase:
  def __init__(self):
    self.firebaseConfig = {
      "apiKey": "",
      "authDomain": "",
      "databaseURL": "",
      "projectId": "rasa-sample-bot",
      "storageBucket": "",
      "messagingSenderId": "",
      "appId": "",
      "measurementId": ""
    }

    self.firebase = pyrebase.initialize_app(self.firebaseConfig)

    self.db = self.firebase.database()

  def write_data(self,userid,data,identifier):
    print(type(data))
    self.db = self.firebase.database()
    self.db.child("people").child(userid).child(identifier).set(data)  #creating user details in firebase

  def read_data(self,userid,identifier):
    read_obj = self.db.child('people').child(userid).child(identifier).get()
    return read_obj

  def remove_data(self,userid,identifier):
    read_obj = self.db.child('people').child(userid).child(identifier).remove()
