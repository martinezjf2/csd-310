


from hashlib import new
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.oe6fd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
# print(db.list_collection_names())

# MongoDB insert_one() Task

# Get access to the students collection Resource: https://www.w3schools.com/python/python_mongodb_insert.asp
students = db["students"] 
# print(students)

thorin = {"student_id": "1007", "first_name": "Thorin", "last_name": "Oakenshield"}
bilbo = {"student_id": "1008", "first_name": "Bilbo", "last_name": "Baggins"}
frodo = {"student_id": "1009", "first_name": "Frodo", "last_name": "Baggins"}


first_student = students.insert_one(thorin).inserted_id
second_student = students.insert_one(bilbo).inserted_id
third_student = students.insert_one(frodo).inserted_id

print("\n- - INSERT STATEMENTS - - ")
print(f"Inserted student record {thorin['first_name']} {thorin['last_name']} into the students collection with document id {first_student}")
print(f"Inserted student record {bilbo['first_name']} {bilbo['last_name']} into the students collection with document id {second_student}")
print(f"Inserted student record {frodo['first_name']} {frodo['last_name']} into the students collection with document id {third_student}")
print("\nEnd of program, press any key to exit....\n")

# Resource on f-string and using brackets within the f strings: https://zetcode.com/python/fstring/

