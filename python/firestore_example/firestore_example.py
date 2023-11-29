import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("C:/Users/ehar/OneDrive - St. Lawrence University/CS345Fall23/" +
                               "cs345fall23-firebase-adminsdk-sw4jj-5d4fa257cc.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

# Create a document with id
doc_ref = db.collection("laptops").document("2")
doc_ref.set(
    {
        "name": "MacBook Air M2",
        "brand": "Apple",
    }
)

doc_ref = db.collection("laptops").document("1")
doc_ref.set(
    {
        "name": "HP EliteBook Model 1",
        "brand": "HP",
    }
)

doc_ref = db.collection("laptops").document("3")
doc_ref.set(
    {
        "name": "Lenovo IdeaPad Model 2",
        "brand": "Lenovo",
        "tags": ["Popular", "Latest"],
        "order": {"price": 9405.0, "quantity": 2},
    }
)

# autogenerate id
create_time, doc_ref = db.collection("laptops").add(
    {
        "name": "Apple macbook air",
        "brand": "Apple",
    }
)

# get document by id
doc_ref = db.collection("laptops").document("1")
print(doc_ref.get().to_dict())


# Create a collection implicitly
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



