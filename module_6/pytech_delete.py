import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jwmobnq.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students

print("- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
docs = db.students.find({})
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]))
    print()
    
jessica = {
        "student_id": "1010",
        "first_name": "Jessica",
        "last_name": "Levine"
}
    
jessica_student_id = students.insert_one(jessica).inserted_id
print("- - INSERT STATEMENTS - -")
print("Inserted student record into the students collection with document id " + str(jessica_student_id))

print("\n- - DISPLAYING STUDENT TEST DOC - -")
doc = db.students.find_one({"student_id":"1010"})
print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]))

db.students.delete_one(jessica)

print("\n- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
docs = db.students.find({})
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]))
    print()
    
input("\nEnd of program, press any key to continue...")
