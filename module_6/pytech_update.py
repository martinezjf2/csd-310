

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.oe6fd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
# print(db.list_collection_names())


# Get access to the students collection
# students = db["students"] 
# print(students)

# MongoDB .find() Method

docs = db.students.find({})

print("\n- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
for doc in docs:
    print(f"\nStudent ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    
myquery = { "student_id": "1007"}
newValues = { "$set": { "last_name": "Martinez" }}
result = db.students.update_one(myquery, newValues)
# Resource: https://www.w3schools.com/python/python_mongodb_update.asp



# MongoDB .find_one() Method
    
print("\n- - DISPLAYING STUDENT DOCUMENT 1007 - -")

# Resource: 
# https://www.w3schools.com/python/python_mongodb_find.asp
# https://www.geeksforgeeks.org/python-mongodb-find_one-query/
individual = db.students.find_one({"student_id": "1007"})
# print(individual)

print(f"\nStudent ID: {individual['student_id']}")
print(f"First Name: {individual['first_name']}")
print(f"Last Name: {individual['last_name']}")
    
    
print("\n\nEnd of program, press any key to continue...\n")