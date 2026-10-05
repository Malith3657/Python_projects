

book_names = ["science", "Maths", "History", "Religion"]

print(book_names[0])

book_names[3] = "Geography"

print(book_names[3])

print(book_names[-1])#Accessing the last element

print(book_names[-2])#Access element before last element

print("==================")

for book_name in book_names:
    print(book_name)

print("==================")

print(len(book_names))

book_names.append("Atomic Habits")

print(book_names[-1])

print("===================")

book_names[0] , book_names[-1] = book_names[-1],book_names[0]
for book_name in book_names:
    print(book_name)

print("=====================")

book_names.insert(1,"SILO")
print(book_names)

print("====================")

del book_names[0]
print("After deleting",book_names)

if "Maths" in book_names:
    book_names.remove("Maths")
    print(f"\n{book_names}")

print("==================")

