age = 20 #Dynamically type language
name = "Malith"
is_Married = True
height = 5.6
town = "Kurunagala"


print(name)
print(age)

name = "Madushan"

print(f"\nAfter the value :- {name}\n")

name = "Malith"

print(name , age , height, is_Married , sep=' | ')

print("\n========================\n")

print("\nMy name is ",name)
print("\nI am ",age, "years old\n")
print("I live in " + town)


#type conversions

print("\n======================\n")

print(type(name))
print(type(5.2))
print(type(True))
num1 = "56"

print(type(num1))


print(num1 , type(int(num1)))


print(str(58))

print(float(5))

print("===============")

print(int(True))
print(int(False))

#int() - converts any data types into integer
#str()  - converters any data type into strings
#float - converters any data type into decimals(float)

print("==============")

print(bool("ABC"))
print(bool(0))
print(bool(154))
print(bool(1.0))

#boolean fals value = 0 , 0.0 , Fals , "" , '' , none





