


from hashlib import new
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.oe6fd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
# print(db.list_collection_names())

# MongoDB .find() Task

# Get access to the students collection Resource: https://www.w3schools.com/python/python_mongodb_insert.asp
students = db["students"] 
# print(students)

docs = db.students.find({})

print("\n- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
for doc in docs:
    print(f"\nStudent ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    

# MongoDB .find_one() Task

print("\n- - DISPLAYING STUDENTS DOCUMENT FROM find_one() QUERY - -")
doc = students.find_one({"student_id": "1007"})
print(f"\nStudent ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n")
print("\nEnd of program, press any key to exit....\n")



# BONUS UNCOMMENT TO SEE RESULTS
# MongoDB Delete All Documents Resource Used: https://www.w3schools.com/python/python_mongodb_delete.asp

# print("\n- - DISPLAYING TOTAL NUMBER OF DOCUMENTS DELETED USING THE delete_many() - -")
# doc = students.delete_many({})
# print(f"\nTotal Number of Documents Deleted: {doc.deleted_count}\n")