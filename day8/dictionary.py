student = {
    "name" : "Malith",
    "age" : 20,
    "married" : True,
    "address" : "kurunagala",
    "contact" : ["0716498201","0761843570"]
}
student["contact"].append("07711111111")


print(student["name"])
print(student["contact"])
print(student['married'])

print("\n============================\n")

for m in student:#iterating over the keys
    print(student[m])

print("\n=============================\n")

for contact_no in student["contact"]:
    print(f"contact {contact_no}")

print("\n=============================\n")

for val in student.values():
    print(val)

print("\n=============================\n")

for key,val in student.items():
    print(f"key - {key}  and val - {val}")

print("\n=============================\n")

student["name"] = "Amal"
print(student["name"])

print("\n=============================\n")

for key,val in student.items():
    print(f"key - {key}  and val - {val}")

del student["age"]#Deleting a key value pair from a dictionary

print("\n=============================\n")

for key,val in student.items():
    print(f"key - {key}  and val - {val}")





