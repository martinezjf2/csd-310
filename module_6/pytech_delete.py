



from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.oe6fd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
# print(db.list_collection_names())
# Get access to the students collection Resource: https://www.w3schools.com/python/python_mongodb_insert.asp
# students = db["students"] 
# print(students)

# MongoDB .find() Method

docs = db.students.find({})

print("\n\n- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
for doc in docs:
    print(f"\nStudent ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
print("\n")


# MongoDB .insert_one Method

fernandez = {"student_id": "1010", "first_name": "Fernandez", "last_name": "Torres"}
fourth_student = db.students.insert_one(fernandez).inserted_id

print("\n- - INSERT STATEMENTS - - \n")
print(f"Inserted student record {fernandez['first_name']} {fernandez['last_name']} into the students collection with document id {fourth_student}\n")



# MongoDB .find_one() Method

print("\n- - DISPLAYING STUDENT TEST DOC - -")
doc = db.students.find_one({"student_id": "1010"})
print(f"\nStudent ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n")


# MongoDB .delete_one() Method
query = {"student_id": "1010"}
student = db.students.delete_one(query)



print("\n- - DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY - -")
documents = db.students.find({})

for doc in documents:
    print(f"\nStudent ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
print("\n\nEnd of program, press any key to continue...\n")







