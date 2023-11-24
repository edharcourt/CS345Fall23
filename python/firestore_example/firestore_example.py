import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("C:/Users/ehar/OneDrive - St. Lawrence University/CS345Fall23/" +
                               "cs345fall23-firebase-adminsdk-sw4jj-5d4fa257cc.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

students = db.collection(u'students')

"""
docs = students.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
"""

# A collection is a collection of documents
doc = students.document(u'student1')

student1 = \
    {
        "courses": {

            "c1" : {
                "coursenum": "H101",
                "title": "Herbology",
                "semester": "Spring",
                "year": 2009
            },

            "c2" :{
                "coursenum": "C101",
                "title": "Charms",
                "semester": "Spring",
                "year": 2008
            }
        },
        "name": {"first": "Ron", "last": "Weasley"}
    }

#doc.set(student1)

s = json.dumps(student1, indent=4)
print(s)

doc = students.document(u'student2')
doc.set(
    {
        "courses" : [{"coursenum" : "H101",
                      "title" : "Herbology",
                      "semester" : "Spring",
                      "year" : 2009},

                     {"coursenum" : "C101",
                      "title" : "Charms",
                      "semester" : "Spring",
                      "year" : 2008}],
        "name" : {"first" : "Ron", "last" : "Weasley"}
    }
)

# Update a document
doc.update({u'name.first' : u'Ronald'})

# Delete a document
#doc.delete()



