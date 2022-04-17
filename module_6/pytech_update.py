

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.oe6fd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
# print(db.list_collection_names())



# Get access to the students collection Resource: https://www.w3schools.com/python/python_mongodb_insert.asp
# students = db["students"] 
# print(students)

# MongoDB .find() Task

docs = db.students.find({})

print("\n- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
for doc in docs:
    print(f"\nStudent ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    
print("\n\nEnd of program, press any key to continue...\n")