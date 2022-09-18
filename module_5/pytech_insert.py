import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jwmobnq.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students

fred = {
        "student_id": "1007",
        "first_name": "Fred",
        "last_name": "Jones"
    }
jane = {
        "student_id": "1008",
        "first_name": "Jane",
        "last_name": "Doe"
    }
tim = {
        "student_id": "1009",
        "first_name": "Tim",
        "last_name": "Barnes"
    }

print("- - INSERT STATEMENTS - -")
fred_student_id = students.insert_one(fred).inserted_id
print("Inserted student record Fred Jones into the students collection with document id " + str(fred_student_id))

jane_student_id = students.insert_one(jane).inserted_id
print("Inserted student record Jane Doe into the students collection with document id " + str(jane_student_id))

tim_student_id = students.insert_one(tim).inserted_id
print("Inserted student record Tim Barnes into the students collection with document id " + str(tim_student_id))

input("\nEnd of program, press any key to exit... ")
