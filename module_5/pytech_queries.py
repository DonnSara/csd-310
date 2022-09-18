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

print("- - DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY - -")
doc = db.students.find_one({"student_id":"1007"})
print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]))

input("\nEnd of program, press any key to continue...")
